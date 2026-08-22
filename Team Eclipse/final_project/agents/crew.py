import os
import yaml
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import HuggingFaceEndpoint
from agents.custom_tools import ChromaDBSearchTool

class ProctoringCrew:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        with open(os.path.join(base_dir, "config/agents.yaml"), "r") as f:
            self.agents_config = yaml.safe_load(f)
        with open(os.path.join(base_dir, "config/tasks.yaml"), "r") as f:
            self.tasks_config = yaml.safe_load(f)

        self.llm = HuggingFaceEndpoint(
            repo_id=os.getenv("HF_MODEL_ID", "google/gemma-3-12b-it"),
            endpoint_url=os.getenv("HF_ROUTER_BASE_URL"),
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            temperature=0.1
        )

    def run(self, vision_data: dict, audio_data: dict) -> str:
        vision_agent = Agent(
            config=self.agents_config["vision_analyst"],
            llm=self.llm,
            verbose=False
        )
        audio_agent = Agent(
            config=self.agents_config["audio_transcript_analyst"],
            llm=self.llm,
            verbose=False
        )
        evaluator_agent = Agent(
            config=self.agents_config["incident_evaluator"],
            tools=[ChromaDBSearchTool()],
            llm=self.llm,
            verbose=False
        )

        task_vision = Task(
            config=self.tasks_config["evaluate_vision_telemetry"],
            agent=vision_agent
        )
        task_audio = Task(
            config=self.tasks_config["evaluate_audio_telemetry"],
            agent=audio_agent
        )
        task_eval = Task(
            config=self.tasks_config["assess_exam_integrity"],
            agent=evaluator_agent
        )

        crew = Crew(
            agents=[vision_agent, audio_agent, evaluator_agent],
            tasks=[task_vision, task_audio, task_eval],
            process=Process.sequential,
            verbose=False
        )

        result = crew.kickoff(inputs={
            "vision_data": str(vision_data),
            "audio_data": str(audio_data)
        })

        return str(result)

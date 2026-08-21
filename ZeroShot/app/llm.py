"""
Setup:
    GEMINI_API_KEY=...     
    ollama server            
"""

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)
from langchain_ollama import (
    ChatOllama
)
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from langchain_core.runnables import (
    RunnableLambda
)

VALID_PROVIDERS = (
    "gemini",
    "ollama"
)


class LocalLLM:

    def __init__(
        self,
        gemini_model="gemini-3.6-flash",
        gemini_api_key=None,
        ollama_model="llama3.2:1b",
        ollama_base_url="http://localhost:11434",
        temperature=0,
        default_provider="gemini"
    ):

        self.gemini_model_name = gemini_model
        self.ollama_model_name = ollama_model

        self.gemini_configured = bool(
            gemini_api_key
        )

        self._gemini_client = ChatGoogleGenerativeAI(
            model=gemini_model,
            google_api_key=gemini_api_key or "not-configured",
            temperature=temperature
        )

        self._ollama_client = ChatOllama(
            model=ollama_model,
            base_url=ollama_base_url,
            temperature=temperature
        )

        self._provider = (
            default_provider
            if default_provider in VALID_PROVIDERS
            else "gemini"
        )

        self.llm = RunnableLambda(
            self._dispatch
        )

     
    # DISPATCH (used by the .llm Runnable proxy)
     

    def _active_client(
        self
    ):

        if self._provider == "ollama":

            return self._ollama_client

        return self._gemini_client

    def _dispatch(
        self,
        input,
        config=None
    ):

        if (
            self._provider == "gemini"
            and not self.gemini_configured
        ):

            raise RuntimeError(
                "GEMINI_API_KEY is not set. Switch to the Ollama "
                "provider, or set GEMINI_API_KEY, before using "
                "chat/RAG features."
            )

        return self._active_client().invoke(
            input
        )

     
    # PROVIDER SWITCHING
     

    @property
    def provider(
        self
    ):

        return self._provider

    def switch(
        self,
        provider
    ):

        if provider not in VALID_PROVIDERS:

            raise ValueError(
                f"Unknown provider '{provider}'. "
                f"Must be one of {VALID_PROVIDERS}."
            )

        if (
            provider == "gemini"
            and not self.gemini_configured
        ):

            raise RuntimeError(
                "Cannot switch to Gemini: GEMINI_API_KEY is not "
                "configured."
            )

        self._provider = provider

    def status(
        self
    ):

        return {

            "active_provider":
                self._provider,

            "gemini": {
                "model": self.gemini_model_name,
                "configured": self.gemini_configured
            },

            "ollama": {
                "model": self.ollama_model_name,
                "configured": True
            }
        }

     
    # INVOKE
     

    def invoke(
        self,
        system_prompt,
        user_prompt
    ):

        if (
            self._provider == "gemini"
            and not self.gemini_configured
        ):

            raise RuntimeError(
                "GEMINI_API_KEY is not set. Switch to the Ollama "
                "provider, or set GEMINI_API_KEY, before using "
                "chat/RAG features."
            )

        messages = [

            SystemMessage(
                content=system_prompt
            ),

            HumanMessage(
                content=user_prompt
            )

        ]

        response = (
            self._active_client().invoke(
                messages
            )
        )

        return response.content

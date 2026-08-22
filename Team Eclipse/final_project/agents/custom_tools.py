from crewai.tools import BaseTool
from backend.vectordb.client import get_chroma_client
from backend.vectordb.embeddings import get_local_embedding_function

class ChromaDBSearchTool(BaseTool):
    name: str = "ChromaDB Exam Rule Search Tool"
    description: str = "Searches embedded exam rules and guidelines stored in the local ChromaDB vector database."

    def _run(self, query: str) -> str:
        client = get_chroma_client()
        embedding_fn = get_local_embedding_function()
        
        col = client.get_or_create_collection(
            name="exam_rules",
            embedding_function=embedding_fn
        )
        
        results = col.query(
            query_texts=[query],
            n_results=2
        )
        
        if not results["documents"] or not results["documents"][0]:
            return "No matching exam rules found."
            
        docs = results["documents"][0]
        return "Matched Exam Rules:\n" + "\n".join([f"- {doc}" for doc in docs])

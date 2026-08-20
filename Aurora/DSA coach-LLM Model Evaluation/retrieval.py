from sqlalchemy import text
from db import engine
from model import llm, embeddings

def semantic_search(query, top_k=5):
    query_vector = embeddings.embed_query(query)
    with engine.connect() as conn:
        results = conn.execute(
            text("""
                SELECT r.id, r.content,
                       e.embedding <-> CAST(:q AS vector) AS distance
                FROM raw_documents r
                JOIN document_embeddings e ON r.id = e.raw_id
                ORDER BY e.embedding <-> CAST(:q AS vector)
                LIMIT :k
            """),
            {"q": str(query_vector), "k": top_k}
        )
        rows = results.fetchall()
    return rows

def hybrid_search(query, top_k=5):
    query_vector = embeddings.embed_query(query)
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT r.id, r.content,
                       (1 - (e.embedding <=> CAST(:query_vector AS vector))) AS semantic_score,
                       ts_rank_cd(to_tsvector('english', r.content),
                                  plainto_tsquery('english', :query)) AS keyword_score
                FROM raw_documents r
                JOIN document_embeddings e ON r.id = e.raw_id
                WHERE to_tsvector('english', r.content) @@ plainto_tsquery('english', :query)
                   OR e.embedding <=> CAST(:query_vector AS vector) < 0.9
                ORDER BY ((1 - (e.embedding <=> CAST(:query_vector AS vector))) * 0.7
                          + ts_rank_cd(to_tsvector('english', r.content),
                                       plainto_tsquery('english', :query)) * 0.3) DESC
                LIMIT :top_k
            """),
            {"query_vector": str(query_vector), "query": query, "top_k": top_k}
        )
        rows = result.fetchall()
    return rows

def search_and_answer(query, mode="hybrid", top_k=5, history=None, model_name="gemini"):
    results = semantic_search(query, top_k) if mode == "semantic" else hybrid_search(query, top_k)
    context_chunks = [row.content for row in results]
    context = "\n\n".join(context_chunks)

    conversation = ""
    if history:
        for message in history[-10:]:
            role = message.get("role")
            content = message.get("content")
            if role == "user":
                conversation += f"User: {content}\n"
            elif role == "assistant":
                conversation += f"DSA Coach: {content}\n"

    prompt = f"""
You are DSA Coach, a friendly and helpful Data Structures tutor.

KNOWLEDGE BASE:
{context}

PREVIOUS CONVERSATION:
{conversation}

CURRENT QUESTION:
{query}

Give only the helpful answer to the current question.
"""

    chosen_llm = llm.get(model_name)
    if chosen_llm is None:
        raise ValueError(f"Model '{model_name}' not found. Choose from: {list(llm.keys())}")

    response = chosen_llm.invoke(prompt)

    if isinstance(response.content, str):
        answer = response.content
    elif isinstance(response.content, list):
        answer = "\n".join(
            item["text"] if isinstance(item, dict) and "text" in item else str(item)
            for item in response.content
        )
    else:
        answer = str(response.content)

    return answer

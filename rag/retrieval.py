from rag.embeddings import generate_embedding
from rag.faiss_store import search_documents


def retrieve_context(
    query_text
):

    query_embedding = generate_embedding(
        query_text
    )

    results = search_documents(
        query_embedding
    )

    return "\n".join(results)
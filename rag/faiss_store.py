import faiss
import numpy as np

DIMENSION = 384

index = faiss.IndexFlatL2(
    DIMENSION
)

document_store = {}


def add_document(
    doc_id,
    text,
    embedding
):

    embedding = np.array(
        [embedding]
    ).astype("float32")

    index.add(embedding)

    document_store[
        index.ntotal - 1
    ] = text


def search_documents(
    query_embedding,
    k=5
):

    query_embedding = np.array(
        [query_embedding]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:

        if idx in document_store:
            results.append(
                document_store[idx]
            )

    return results
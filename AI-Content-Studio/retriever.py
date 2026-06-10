from vector_store import embedding_model
import numpy as np


def retrieve_relevant_chunks(query, index, chunks):

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k=3
    )

    results = [chunks[i] for i in indices[0]]

    return results
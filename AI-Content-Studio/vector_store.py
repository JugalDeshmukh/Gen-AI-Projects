from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def split_text_into_chunks(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def create_embeddings(chunks):

    embeddings = embedding_model.encode(chunks)

    return embeddings


def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index
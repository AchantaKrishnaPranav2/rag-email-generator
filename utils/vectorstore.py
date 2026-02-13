import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vectorstore(texts):

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    with open("vectorstore/texts.pkl", "wb") as f:
        pickle.dump(texts, f)

    faiss.write_index(index, "vectorstore/index.faiss")

def retrieve(query, k=3):

    index = faiss.read_index("vectorstore/index.faiss")

    with open("vectorstore/texts.pkl", "rb") as f:
        texts = pickle.load(f)

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, k)

    results = [texts[i] for i in indices[0]]

    return results


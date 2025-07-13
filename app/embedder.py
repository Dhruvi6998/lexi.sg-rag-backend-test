from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX_PATH = "faiss.index"
META_PATH = "metadata.json"

def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def build_index(docs):
    vectors, metadata = [], []
    for doc in docs:
        chunks = chunk_text(doc["text"])
        for i, chunk in enumerate(chunks):
            emb = model.encode(chunk)
            vectors.append(emb)
            metadata.append({"source": doc["source"], "text": chunk})

    vectors_np = np.array(vectors).astype("float32")
    index = faiss.IndexFlatL2(vectors_np.shape[1])
    index.add(vectors_np)

    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "w") as f:
        json.dump(metadata, f)

def load_index():
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH) as f:
        metadata = json.load(f)
    return index, metadata, model

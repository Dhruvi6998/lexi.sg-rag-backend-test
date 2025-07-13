from app.embedder import load_index
from app.llm import ask_llm
import numpy as np

index = None
metadata = None
model = None

def query_rag(user_query, top_k=3):
    global index, metadata, model

    # Load FAISS index and metadata only when needed
    if index is None or metadata is None or model is None:
        index, metadata, model = load_index()

    query_emb = model.encode(user_query).astype("float32")
    D, I = index.search(np.array([query_emb]), top_k)

    selected = [metadata[i] for i in I[0]]
    context = "\n".join([f"{s['text']} (Source: {s['source']})" for s in selected])
    answer = ask_llm(context, user_query)

    citations = [{"text": s["text"], "source": s["source"]} for s in selected]
    return {"answer": answer, "citations": citations}
from fastapi import FastAPI
from pydantic import BaseModel
from app.document_loader import load_documents
from app.embedder import build_index
from app.rag_pipeline import query_rag
import os

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.on_event("startup")
def initialize():
    if not os.path.exists("faiss.index"):
        docs = load_documents("data/legal_docs")
        build_index(docs)

@app.post("/query")
def handle_query(payload: QueryInput):
    return query_rag(payload.query)
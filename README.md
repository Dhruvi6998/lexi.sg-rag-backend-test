This project is a **legal question answering backend** using **FastAPI** and a **free, local AI model**. It reads your `.pdf` or `.docx` legal documents, finds relevant parts, and generates an answer.

---

## 📁 Folder Structure

```
lexi.sg-rag-backend-test/
├── app/                     # All the Python code
│   ├── main.py              # FastAPI API routes
│   ├── document_loader.py   # Loads and reads DOCX and PDF
│   ├── embedder.py          # Embeds document chunks with FAISS
│   ├── rag_pipeline.py      # Runs the query-retrieve-generate logic
│   └── llm.py               # The AI model (e.g., flan-t5-large)
│
├── data/legal_docs/         # 📥 Add your legal documents here
├── requirements.txt         # All required Python libraries
├── README.md                # This guide
```

### Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows



###  Start the Server
```bash
uvicorn app.main:app --reload
```
Visit:
👉 http://127.0.0.1:8000/docs

---

## 📬 Using the `/query` Endpoint

### Method: `POST`
### URL: `http://127.0.0.1:8000/query`

Create data/legal_docs/ to add all the documents

Requirements

fastapi
uvicorn
sentence-transformers
faiss-cpu
python-docx
PyMuPDF
transformers
torch


import os
from docx import Document
import fitz  # PyMuPDF

def load_docx_text(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

def load_pdf_text(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def load_documents(folder):
    texts = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if filename.endswith(".docx"):
            content = load_docx_text(path)
        elif filename.endswith(".pdf"):
            content = load_pdf_text(path)
        else:
            continue
        texts.append({"text": content, "source": filename})
    return texts

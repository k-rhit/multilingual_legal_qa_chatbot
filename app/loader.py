import os
from PyPDF2 import PdfReader
from docx import Document

def load_text_from_files(folder_path="data/legal_docs"):
    text = ""
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith(".pdf"):
            reader = PdfReader(full_path)
            for page in reader.pages:
                text += page.extract_text() or ""
        elif file.endswith(".docx"):
            doc = Document(full_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file.endswith(".txt"):
            with open(full_path, "r", encoding="utf-8") as f:
                text += f.read() + "\n"
    return text

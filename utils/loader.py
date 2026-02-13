import os
import pandas as pd
from pypdf import PdfReader
from docx import Document

def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def load_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def load_txt(file):
    return file.read().decode("utf-8")

def load_excel(file):
    df = pd.read_excel(file)
    return df.to_string()

def load_file(file):
    name = file.name.lower()

    if name.endswith(".pdf"):
        return load_pdf(file)

    elif name.endswith(".docx"):
        return load_docx(file)

    elif name.endswith(".txt"):
        return load_txt(file)

    elif name.endswith(".xlsx"):
        return load_excel(file)

    return ""


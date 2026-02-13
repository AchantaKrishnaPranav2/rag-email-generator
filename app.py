import streamlit as st
import pandas as pd
import os

from utils.loader import load_file
from utils.vectorstore import create_vectorstore
from utils.generator import generate_email

st.title("RAG Email Generator (Free, Local)")

# Upload documents
uploaded_files = st.file_uploader(
    "Upload documents",
    accept_multiple_files=True
)

if st.button("Process Documents"):

    texts = []

    for file in uploaded_files:
        text = load_file(file)
        texts.append(text)

    os.makedirs("vectorstore", exist_ok=True)

    create_vectorstore(texts)

    st.success("Documents processed")


# Persona upload
persona_file = st.file_uploader("Upload Persona Excel", type=["xlsx"])

persona = ""

if persona_file:

    df = pd.read_excel(persona_file)

    person = st.selectbox("Select Persona", df.iloc[:,0])

    persona = df[df.iloc[:,0] == person].to_string()


# Cadence input
cadence = st.text_area("Cadence")

# Goal
goal = st.text_input("What do you want to generate?")


if st.button("Generate Email"):

    result = generate_email(persona, cadence, goal)

    st.write(result)


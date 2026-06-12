import streamlit as st
import fitz  # PyMuPDF for PDFs
from docx import Document  # for .docx files

def extract_text(file):
    file_extension = file.name.split('.')[-1].lower()
    text = ""
    
    if file_extension == 'pdf':
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    elif file_extension == 'docx':
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        text = file.read().decode("utf-8")
    return text

st.set_page_config(page_title="Universal Portfolio", layout="wide")
st.title("📂 Universal Portfolio Generator")

uploaded_file = st.file_uploader("Upload your CV (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("Extracting content..."):
        content = extract_text(uploaded_file)
        
    st.header("Generated Preview")
    
    # Simple dynamic rendering
    st.text_area("Full Extracted Content", value=content, height=400)
    
    if st.button("Generate Professional Website Layout"):
        # Here you can trigger an AI function to format the 'content' string
        st.write("Layout logic goes here (e.g., using Gemini API to structure your data).")
        st.success("Portfolio layout generated!")

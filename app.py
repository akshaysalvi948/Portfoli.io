import streamlit as st
import fitz  # PyMuPDF
from docx import Document
import urllib.parse

# --- PAGE SETUP ---
st.set_page_config(page_title="Portfoli.io", layout="wide")

# --- INITIALIZE SESSION STATE ---
if 'portfolio_data' not in st.session_state:
    st.session_state.portfolio_data = None

# --- PARSING ENGINE ---
def extract_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'pdf':
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif ext == 'docx':
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return file.read().decode("utf-8")

# --- UI: LANDING PAGE (UPLOADER) ---
if st.session_state.portfolio_data is None:
    st.title("🚀 Portfoli.io")
    st.subheader("Transform your CV into a professional web presence in seconds.")
    uploaded_file = st.file_uploader("Upload your CV to begin", type=["pdf", "docx", "txt"])
    
    if uploaded_file and st.button("Generate My Portfolio"):
        with st.spinner("Forging your digital identity..."):
            st.session_state.portfolio_data = extract_text(uploaded_file)
            st.rerun() # Magic command that refreshes the page and triggers the Portfolio UI

# --- UI: FANCY STARLINK-INSPIRED PORTFOLIO PAGE ---
else:
    # Applying Starlink CSS
    st.markdown("""<style>
        .main { background: #0a0a0a; color: white; }
        .hero { font-family: 'Inter', sans-serif; font-size: 48px; letter-spacing: 8px; text-transform: uppercase; text-align: center; margin-top: 100px; }
        .content-card { background: rgba(255,255,255,0.05); padding: 40px; border-radius: 0px; border: 1px solid #333; }
    </style>""", unsafe_allow_html=True)

    st.markdown('<div class="hero">DIGITAL IDENTITY</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.subheader("Extracted Professional Profile")
    st.write(st.session_state.portfolio_data)
    
    if st.button("⬅️ Upload Another CV"):
        st.session_state.portfolio_data = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

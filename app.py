import streamlit as st
import fitz 
from docx import Document

# --- PAGE CONFIG ---
st.set_page_config(page_title="Portfoli.io | Professional", layout="wide")

# --- STARLINK-INSPIRED DARK MODE STYLING ---
st.markdown("""
    <style>
    .main { background: #050505; color: #ffffff; }
    .hero { font-family: 'Inter', sans-serif; font-size: 50px; letter-spacing: 12px; text-transform: uppercase; text-align: center; margin: 80px 0; }
    .card { background: rgba(255,255,255,0.03); padding: 40px; border: 1px solid #222; margin-bottom: 20px; }
    .btn { background: white !important; color: black !important; border-radius: 0px !important; text-transform: uppercase; font-weight: bold; letter-spacing: 2px; }
    </style>
""", unsafe_allow_html=True)

# --- BACKEND: EXTRACTOR ---
def get_cv_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'pdf':
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif ext == 'docx':
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    return file.read().decode("utf-8")

# --- APP LOGIC ---
if 'cv_content' not in st.session_state:
    st.session_state.cv_content = None

if st.session_state.cv_content is None:
    st.markdown("<div class='hero'>PORTFOLI.IO</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        uploaded_file = st.file_uploader("UPLOAD CV (PDF/DOCX)", type=["pdf", "docx", "txt"])
        if uploaded_file and st.button("GENERATE PORTFOLIO", use_container_width=True):
            with st.spinner("Engineering your digital presence..."):
                st.session_state.cv_content = get_cv_text(uploaded_file)
                st.rerun()
else:
    # --- DYNAMIC PORTFOLIO VIEW ---
    st.markdown("<div class='hero'>AKSHAY SALVI</div>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 2])
    with col_l:
        st.markdown("<div class='card'><h3>SUMMARY</h3><p>Senior Data Engineer with 8+ years of experience.</p></div>", unsafe_allow_html=True)
    with col_r:
        st.markdown("<div class='card'><h3>EXPERIENCE</h3><p>"+ st.session_state.cv_content[:500] +"...</p></div>", unsafe_allow_html=True)
    
    if st.button("⬅️ START OVER"):
        st.session_state.cv_content = None
        st.rerun()

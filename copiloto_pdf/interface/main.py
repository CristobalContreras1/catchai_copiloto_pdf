import streamlit as st
import pdfplumber
import os
import sys

# Agrega la carpeta 'app' al path para importar ingestion.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from ingestion import process_pdf_text

st.set_page_config(page_title="Copiloto PDF", layout="wide")
st.title("📄 Copiloto PDF")
st.markdown("Sube un archivo PDF y te ayudaré a procesarlo en fragmentos útiles.")

# Cargar archivo PDF
uploaded_file = st.file_uploader("Selecciona un archivo PDF", type="pdf")

if uploaded_file is not None:
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            raw_text = ''
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    raw_text += page_text + '\n'

        if raw_text.strip() == '':
            st.warning(" No se pudo extraer texto del PDF. ¿Está escaneado como imagen?")
        else:
            st.success("✅ Texto extraído correctamente.")

            # Procesar texto con ingestion.py
            chunks = process_pdf_text(raw_text)

            st.subheader("🧠 Fragmentos procesados")
            for i, chunk in enumerate(chunks):
                st.markdown(f"**Chunk {i+1}:**")
                st.write(chunk)

    except Exception as e:
        st.error(f"❌ Error al procesar el PDF: {e}")
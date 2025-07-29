import streamlit as st
from PIL import Image
import numpy as np
import pytesseract

st.set_page_config(page_title="OCR com Tesseract", layout="centered")
st.title("🖼️ OCR JPEG usando Tesseract (offline)")

uploaded_file = st.file_uploader("📤 Envie uma imagem (JPEG, JPG, PNG)", type=["jpeg", "jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    max_width = 1000
    if image.width > max_width:
        new_height = int(image.height * (max_width / image.width))
        image = image.resize((max_width, new_height))

    st.image(image, caption="🖼️ Imagem carregada", use_container_width=True)
    img_np = np.array(image)

    with st.spinner("🔍 Realizando OCR com Tesseract..."):
        try:
            parsed_text = pytesseract.image_to_string(img_np, lang="por")
            parsed_text = parsed_text.strip()
            if not parsed_text:
                st.warning("⚠️ Nenhum texto detectado")
            else:
                st.subheader("📑 Texto Detectado:")
                st.code(parsed_text)

                palavras = parsed_text.split()
                percentual = min(100, len(palavras) * 5)
                st.subheader("📊 Porcentagem Estimada de Leitura")
                st.progress(percentual / 100)
                st.write(f"**Leitura estimada: {percentual:.2f}%**")
        except Exception as e:
            st.error("❌ Erro ao realizar OCR com Tesseract")
            st.text(f"Detalhes técnicos: {e}")

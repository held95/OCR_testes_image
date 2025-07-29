import streamlit as st
from PIL import Image
import io
import easyocr
import numpy as np

st.set_page_config(page_title="OCR com EasyOCR", layout="centered")
st.title("🖼️ OCR JPEG usando EasyOCR (offline)")

uploaded_file = st.file_uploader("📤 Envie uma imagem (JPEG, JPG, PNG)", type=["jpeg", "jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")  # Garante imagem RGB

    # Redimensiona se a imagem for muito grande
    max_width = 1000
    if image.width > max_width:
        new_height = int(image.height * (max_width / image.width))
        image = image.resize((max_width, new_height))

    st.image(image, caption="🖼️ Imagem carregada", use_container_width=True)

    # Converte para array (formato compatível com EasyOCR)
    img_np = np.array(image)

    with st.spinner("🔍 Realizando OCR na imagem com EasyOCR..."):
        try:
            reader = easyocr.Reader(['pt'], gpu=False)
            results = reader.readtext(img_np, detail=0, paragraph=True)
            parsed_text = "\n".join(results).strip()

            if not parsed_text:
                st.warning("⚠️ Nenhum texto detectado.")
            else:
                st.subheader("📑 Texto Detectado:")
                st.code(parsed_text)

                palavras = parsed_text.split()
                percentual = min(100, len(palavras) * 5)
                st.subheader("📊 Porcentagem Estimada de Leitura")
                st.progress(percentual / 100)
                st.write(f"**Leitura estimada: {percentual:.2f}%**")

        except Exception as e:
            st.error("❌ Erro ao realizar OCR.")
            st.text(f"Detalhes técnicos: {str(e)}")

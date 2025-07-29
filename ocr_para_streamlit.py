import streamlit as st
from PIL import Image
import io
import easyocr

st.set_page_config(page_title="OCR com EasyOCR", layout="centered")
st.title("🖼️ OCR JPEG usando EasyOCR (local)")

uploaded_file = st.file_uploader("Upload de Arquivos", type=["jpeg", "jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")  # Garante que a imagem esteja em RGB

    # Redimensionar imagem se for muito grande (largura máxima = 1000px)
    max_width = 1000
    if image.width > max_width:
        new_height = int(image.height * (max_width / image.width))
        image = image.resize((max_width, new_height))

    st.image(image, caption='Imagem carregada', use_container_width=True)

    # Converter imagem para formato aceito pelo EasyOCR (numpy array)
    import numpy as np
    img_np = np.array(image)

    with st.spinner("🔍 Realizando OCR na imagem..."):
        try:
            # Inicializar leitor EasyOCR para português
            reader = easyocr.Reader(['pt'], gpu=False)  # gpu=True se você quiser usar GPU

            # Realizar leitura OCR
            results = reader.readtext(img_np, detail=0, paragraph=True)

            # results é uma lista de strings (textos detectados)
            parsed_text = "\n".join(results).strip()

            if not parsed_text:
                st.warning("Nenhum texto detectado.")
            else:
                st.subheader("📑 Texto Detectado:")
                st.code(parsed_text)

                # Simulação da porcentagem de leitura
                palavras = parsed_text.split()
                percentual = min(100, len(palavras) * 5)  # Estimativa baseada em quantidade de palavras
                st.subheader("📊 Porcentagem Estimada de Leitura")
                st.progress(percentual / 100)
                st.write(f"Leitura estimada: **{percentual:.2f}%**")

        except Exception as e:
            st.error("⚠️ Erro ao realizar OCR localmente.")
            st.text(f"Detalhes técnicos: {str(e)}")

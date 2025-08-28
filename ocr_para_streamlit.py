import streamlit as st
from PIL import Image
import io
import easyocr
import numpy as np
import zipfile

st.set_page_config(page_title="OCR com EasyOCR", layout="centered")
st.title("🖼️ OCR JPEG usando EasyOCR (offline)")

uploaded_files = st.file_uploader(
    "📤 Envie uma ou mais imagens (JPEG, JPG, PNG)", 
    type=["jpeg", "jpg", "png"], 
    accept_multiple_files=True
)

if uploaded_files:
    reader = easyocr.Reader(['pt'], gpu=False)  # Carrega uma vez só
    
    # Guardar os arquivos TXT em memória
    txt_files = {}

    for idx, uploaded_file in enumerate(uploaded_files, start=1):
        st.markdown(f"### 📌 Imagem {idx}: {uploaded_file.name}")
        
        image = Image.open(uploaded_file).convert("RGB")

        # Redimensiona se a imagem for muito grande
        max_width = 1000
        if image.width > max_width:
            new_height = int(image.height * (max_width / image.width))
            image = image.resize((max_width, new_height))

        st.image(image, caption=f"🖼️ {uploaded_file.name}", use_container_width=True)

        # Converte para array (formato compatível com EasyOCR)
        img_np = np.array(image)

        with st.spinner("🔍 Realizando OCR na imagem..."):
            try:
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

                    # Guarda em dicionário com nome do arquivo
                    txt_files[f"{uploaded_file.name.rsplit('.',1)[0]}.txt"] = parsed_text

            except Exception as e:
                st.error("❌ Erro ao realizar OCR.")
                st.text(f"Detalhes técnicos: {str(e)}")

    # Se houve arquivos processados, gera um ZIP
    if txt_files:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            for filename, content in txt_files.items():
                zipf.writestr(filename, content)
        zip_buffer.seek(0)

        st.download_button(
            label="⬇️ Download ZIP com todos os TXT",
            data=zip_buffer,
            file_name="ocr_textos.zip",
            mime="application/zip"
        )

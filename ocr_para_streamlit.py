import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="OCR com API", layout="centered")
st.title("🖼️ OCR JPEG usando API (OCR.Space)")

API_KEY = "K84757145188957"  # Substitua por sua chave real

uploaded_file = st.file_uploader("Upload de Arquivos", type=["jpeg", "jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")  # Garante que a imagem esteja em RGB

    # Redimensionar imagem se for muito grande (largura máxima = 1000px)
    max_width = 1000
    if image.width > max_width:
        new_height = int(image.height * (max_width / image.width))
        image = image.resize((max_width, new_height))

    st.image(image, caption='Imagem carregada', use_container_width=True)

    # Converter imagem para bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes.seek(0)

    with st.spinner("🔍 Realizando OCR na imagem..."):
        try:
            response = requests.post(
                "https://api.ocr.space/parse/image",
                files={"filename": img_bytes},
                data={"apikey": API_KEY, "language": "por"},
                timeout=30  # segurança contra travamentos
            )
            result = response.json()

            if result.get("IsErroredOnProcessing"):
                st.error("❌ Erro ao processar imagem: " + result.get("ErrorMessage", ["Erro desconhecido"])[0])
            else:
                parsed_text = result["ParsedResults"][0]["ParsedText"]
                st.subheader("📑 Texto Detectado:")
                st.code(parsed_text.strip() or "Nenhum texto detectado.")

                # Simulação da porcentagem de leitura
                palavras = parsed_text.strip().split()
                percentual = min(100, len(palavras) * 5)  # Estimativa baseada em quantidade de palavras
                st.subheader("📊 Porcentagem Estimada de Leitura")
                st.progress(percentual / 100)
                st.write(f"Leitura estimada: **{percentual:.2f}%**")

        except Exception as e:
            st.error("⚠️ Erro na conexão com a API. Verifique a chave ou tente novamente.")
            st.text(f"Detalhes técnicos: {str(e)}")

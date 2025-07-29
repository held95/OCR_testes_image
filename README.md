# 🖼️ OCR JPEG com Streamlit (usando OCR.Space API)

Este projeto é uma aplicação em [Streamlit](https://streamlit.io) que permite fazer upload de imagens `.jpeg`, `.jpg` ou `.png` para realizar **OCR (Reconhecimento Óptico de Caracteres)** usando a **API gratuita OCR.Space**, sem necessidade de instalar Tesseract.

---

## 🔍 Funcionalidades

- Upload de imagens JPEG, JPG ou PNG;
- Leitura de texto com a API OCR.Space;
- Exibição do texto extraído;
- Estimativa da porcentagem de leitura baseada em número de palavras detectadas;
- Compatível com **Streamlit Cloud** (sem dependências do sistema);

---

## 🚀 Como executar o projeto

### 🔧 Requisitos

- Python 3.7+
- Conta gratuita na [OCR.Space](https://ocr.space/OCRAPI) (para obter sua API Key)

### 📦 Instalação

```bash
pip install -r requirements.txt
```

### ▶️ Executar localmente

```bash
streamlit run app.py
```

---

## 🔑 Obter uma API Key gratuita

1. Acesse: https://ocr.space/OCRAPI
2. Clique em **Get Free API Key**
3. Cadastre-se e copie sua chave (ex: `your_api_key_here`)
4. No código, substitua a linha:

```python
API_KEY = "helloworld"
```

por

```python
API_KEY = "your_api_key_here"
```

---

## 📁 Deploy no Streamlit Cloud

1. Envie os arquivos `app.py`, `requirements.txt` e `README.md` para um repositório GitHub;
2. Vá até [https://streamlit.io/cloud](https://streamlit.io/cloud);
3. Conecte com seu GitHub e selecione o repositório;
4. Clique em **Deploy**;
5. Para uso contínuo, edite a variável `API_KEY` com sua chave pessoal.

---

## 🧪 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io)
- [OCR.Space API](https://ocr.space/OCRAPI)
- [Requests (HTTP)](https://docs.python-requests.org/)
- [Pillow (manipulação de imagens)](https://python-pillow.org/)

---

## 📸 Exemplo de Uso

![exemplo](https://i.imgur.com/Bukd8Ac.png)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT.

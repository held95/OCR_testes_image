# 🖼️ OCR JPEG com Streamlit

Este projeto é uma aplicação simples desenvolvida com [Streamlit](https://streamlit.io) que permite fazer upload de imagens no formato `.jpeg` para realizar **OCR (Reconhecimento Óptico de Caracteres)** com a biblioteca `pytesseract`.

## 🔍 Funcionalidades

- Upload de arquivos `.jpeg` ou `.jpg`;
- Leitura de texto da imagem utilizando Tesseract OCR;
- Exibição do texto extraído no terminal do app;
- Estimativa da **porcentagem de leitura** com base nas caixas de texto detectadas;
- Interface amigável e pronta para uso no [Streamlit Cloud](https://streamlit.io/cloud).

---

## 🚀 Como executar o projeto

### 🔧 Requisitos

- Python 3.7+
- Tesseract OCR instalado no sistema (veja abaixo)

### 📦 Instale as dependências

```bash
pip install -r requirements.txt
```

### ▶️ Execute o app

```bash
streamlit run app.py
```

---

## 🧠 Instalação do Tesseract

### Windows

Baixe e instale o executável oficial:

👉 https://github.com/tesseract-ocr/tesseract

Adicione o caminho da instalação ao seu `PATH`. Exemplo:
```
C:\Program Files\Tesseract-OCR
```

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install tesseract-ocr -y
```

---

## 📁 Deploy no Streamlit Cloud

1. Crie um repositório no GitHub e envie os arquivos `app.py`, `requirements.txt` e `README.md`;
2. Acesse [https://streamlit.io/cloud](https://streamlit.io/cloud) e conecte seu GitHub;
3. Escolha o repositório e clique em **Deploy**.

---

## 📸 Exemplo de Uso

![exemplo](https://i.imgur.com/Bukd8Ac.png)

---

## 🧪 Tecnologias

- [Streamlit](https://streamlit.io)
- [Pillow](https://python-pillow.org/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT.


# 🚀 AI Content Studio

AI Content Studio RAG-powered content generation application using Streamlit, FAISS, Sentence Transformers and Hugging Face. It is a Generative AI application built with **Python**, **Streamlit**, and **Retrieval-Augmented Generation (RAG)** techniques. The application allows users to upload PDF documents, extract relevant information, and generate AI-powered content such as LinkedIn posts, blogs, summaries, and more.

---

## 📌 Features

- Upload PDF documents
- Extract text from PDFs
- Split content into chunks
- Generate embeddings using Sentence Transformers
- Store vectors using FAISS
- Retrieve relevant context based on user queries
- Generate AI-powered content
- Customizable content type, tone, and length
- Interactive Streamlit UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- PyPDF2 / pypdf
- Transformers (Hugging Face)
- NumPy

---

## 📂 Project Structure

```text
AI-Content-Studio/
│
├── app.py
├── generator.py
├── pdf_loader.py
├── retriever.py
├── vector_store.py
├── prompt_templates.py
├── requirements.txt
├── README.md
├── screenshots/
```

---

## ⚙️ Workflow

1. Upload PDF documents.
2. Extract text from PDFs.
3. Split text into chunks.
4. Convert chunks into embeddings.
5. Store embeddings using FAISS.
6. Retrieve relevant context.
7. Generate AI content from retrieved information.

---

## 🧠 RAG Architecture

```text
PDF Upload
     ↓
Text Extraction
     ↓
Chunking
     ↓
Sentence Embeddings
     ↓
FAISS Vector Database
     ↓
Context Retrieval
     ↓
LLM Content Generation
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Gen-AI-Projects.git
cd Gen-AI-Projects/AI-Content-Studio
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### PDF Upload

(Add screenshot here)

### Generated Content

(Add screenshot here)

---

## Example Use Cases

- LinkedIn Post Generation
- Blog Writing
- Content Summarization
- Resume-Based Content Creation
- Knowledge Retrieval from PDFs

---

## Future Enhancements

- OpenAI API Integration
- Gemini API Integration
- Multi-document Retrieval
- Chat Interface
- Image Generation Support
- Deployment on Streamlit Cloud

---

## Author

### Jugal Deshmukh

- LinkedIn: https://www.linkedin.com/in/jugaldeshmukh
- GitHub: https://github.com/JugalDeshmukh

---

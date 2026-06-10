#First Major RAG Component File

from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    return text
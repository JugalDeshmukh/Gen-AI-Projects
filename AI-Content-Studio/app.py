import streamlit as st
from generator import generate_content
from pypdf import PdfReader
from pdf_loader import extract_text_from_pdf
from vector_store import (
    split_text_into_chunks,
    create_embeddings,
    create_faiss_index
)
from vector_store import embedding_model
from retriever import retrieve_relevant_chunks


# Page settings
st.set_page_config(
    page_title="AI Content Studio",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 AI Content Studio")
st.subheader("Generate AI-powered content using your documents")

# Sidebar
st.sidebar.header("Content Settings")

content_type = st.sidebar.selectbox(
    "Select Content Type",
    [
        "LinkedIn Post",
        "Professional Email",
        "Blog Outline",
        "Resume Summary",
        "Cover Letter"
    ]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Creative",
        "Formal"
    ]
)

length = st.sidebar.selectbox(
    "Select Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

# Main input
topic = st.text_input("Enter Topic")

keywords = st.text_area(
    "Enter Keywords (comma separated)"
)

# -------------------------
# PDF Upload Section
# -------------------------

st.subheader("📄 Upload Documents")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    pdf_text = extract_text_from_pdf(uploaded_file)
    chunks = split_text_into_chunks(pdf_text)
    embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    st.subheader("Ask Questions About Your PDF")

user_query = st.text_input("Enter your question",key="pdf_question")


if user_query:

    relevant_chunks = retrieve_relevant_chunks(
        user_query,
        index,
        chunks
    )

    st.subheader("Relevant Information")

    context = "\n".join(relevant_chunks)
    prompt = f""" 
    Context:
    {context}
    
    Question:
    {user_query}

    Answer:
    """

    with st.spinner("Generating answer..."):
        answer = generate_content(prompt)

    st.subheader("AI Answer")
    st.write(answer)

    for i, chunk in enumerate(relevant_chunks):

        st.write(f"Result {i+1}")

        st.text_area(
            f"Chunk {i+1}",
            chunk,
            height=120
        )

    st.subheader("FAISS Information")
    st.write("Number of vectors stored:")
    st.write(index.ntotal)

    st.subheader("Extracted Text")

    st.text_area(
    "PDF Content",
    pdf_text,
    height=200
    )

    st.subheader("Generated Chunks")

    for i, chunk in enumerate(chunks):
        st.write(f"Chunk {i+1}")
        
        st.text_area(
        f"Chunk {i+1}",
        chunk,
        height=100
        )
    st.subheader("Embedding Information")

    st.write("Embedding Shape:")

    st.write(embeddings.shape)
    
    st.subheader("Ask Questions About Your PDF")


# Generate button
generate_button = st.button("Generate Content")

# Placeholder output
if generate_button:

    prompt = f"""
    Write a {tone} {content_type}
    about {topic}.

    Keywords:
    {keywords}
    """

    with st.spinner("Generating content..."):
        output = generate_content(prompt)
        #output = "Generation temporarily disabled while building RAG."

    st.subheader("Generated Content")
    st.write(output)
import asyncio
import streamlit as st
from generator import generate_content



# Page settings
st.set_page_config(
    page_title="AI Content Studio",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 AI Content Generator Studio")
st.subheader("Generate AI-powered content using your your favourite topic")

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
        try:
            output = generate_content(prompt)
        except asyncio.CancelledError:
            st.warning("Content generation was canceled. Please try again.")
            output = ""
        except Exception as exc:
            st.error(f"Content generation failed: {exc}")
            output = ""

    if output:
        st.subheader("Generated Content")
        st.write(output)
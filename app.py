import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables (for API key, etc.)
load_dotenv()

# Streamlit App Title
st.title("💬 HuggingFace Chat Web App")

# HuggingFace API Setup
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
model = ChatHuggingFace(llm=llm)

# User Input
user_input = st.text_area("Enter your question or prompt:")

if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            result = model.invoke(user_input)
            st.subheader("Response:")
            st.write(result.content)
    else:
        st.warning("Please enter a prompt first.")

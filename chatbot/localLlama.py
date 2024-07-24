from langchain_community.llms import Ollama
from langchain_core.prompt import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true" # For LangSmith Tracking on LangChain dashboard
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") 

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Query: {query}")
    ]
)

# Streamlit UI
st.titles("LangChain Chatbot")
input_text = st.text_input("Search any topic you want")

# Local LLM with Ollama
llm = Ollama(model = "llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser
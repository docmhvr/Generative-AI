from langchain_openai import ChatOpenAI
from langchain_core.prompt import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
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

# Open AI LLM's
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"query": input_text}))
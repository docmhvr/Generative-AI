from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load env and get API Keys
# For Paid llms and Langchain API for langchain ecosystem config

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

# add_routes(
#     app,
#     # ChatOpenAI(),
#     # path="/openai"
# )

# model = ChatOpenAI()

# Local Ollama Llama2 model
llm = Ollama(model="llama2")

#prompts for local llm
prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
# Define another prompt to test OpenAI model

# Route for local llm model, add more routes for OpenAI/paid llms
add_routes(
    app,
    prompt|llm,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app, host = "localhost", port=8000) #Add more host for more serverss for production


# After running the server with langserve, add "/docs at end of locahost" to get swagger UI documentation
# Swagger documentation =>Langchain server, input and output schemas, api calls !!
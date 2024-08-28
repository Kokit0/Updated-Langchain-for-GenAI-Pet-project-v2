from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate #tenía langchain.prompts pero actualizaron, ahora es langchain_core.prompts
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI # antiguamente corría con esto
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# cargamos la función de variables de entorno (load_dotenv) para inicializar con eso
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()
##ollama llama2
llm=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")
# Nosotros definiremos el {topic} mas adelante

add_routes(
    app,
    prompt1|model,
    path="/essay"


)

add_routes(
    app,
    prompt2|llm,
    path="/poem"


)

# desde acá llamaremos y correremos el uvicorn
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

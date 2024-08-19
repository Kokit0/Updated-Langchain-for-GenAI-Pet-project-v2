from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
)  # parser del output por defecto (pero luego usaré uno custom)

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langsmith tracing (super util para trackear lo que hagamos)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

## Prompt Template (chatbot prompt template for chat duh)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question:{question}"),
    ]
)

## streamlit framework

st.title("Langchain Demo Con OPENAI API")
input_text = st.text_input("Busca sobre el tópico que tu quieras")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo") #integramos ocn el llm
output_parser = StrOutputParser() # con output parser obtenemos el resultado "trozado"
chain = prompt | llm | output_parser # combinamos encadenado, las 3 acciones

if input_text:
    st.write(chain.invoke({"question": input_text}))



"""
Desarrollado por Jorge Amaya S. 2024
"""

from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os

#function to load openai model and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name='gpt-3.5-turbo', temperature = 0.5)
    response=llm(question)
    return response

st.set_page_config(page_title="Q&a DEMO")
st.header("Langchain Application")

input=st.text_input("input: ",key="input")
response=get_openai_response(input)

submit=st.button("ask the question")

if submit ==True:
    st.subheader("the response is")
    st.write("response")

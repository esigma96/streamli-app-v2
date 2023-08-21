import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Page title
st.set_page_config(page_title='🦜🔗 WhatsApp Chat Analysis')
st.title('🦜🔗 WhatsApp Chat Analysis')

# File upload
uploaded_file = st.file_uploader('Upload an article', type='txt')
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Run Analysis', disabled=not(uploaded_file))


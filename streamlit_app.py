import streamlit as st
####Importing Necessary Libraries
import re
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title='🦜🔗 WhatsApp Chat Analysis')
st.title('🦜🔗 WhatsApp Chat Analysis')

# File upload
uploaded_file = st.file_uploader('Upload your chat file', type='txt')
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Run Analysis', disabled=not(uploaded_file))
    #### import datasets
    file = open(r'uploaded_file',mode='r',encoding="utf8")
    data = file.read()
    file.close()
    data

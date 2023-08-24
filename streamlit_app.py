import streamlit as st
####Importing Necessary Libraries
import re
import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title='🦜🔗 WhatsApp Chat Analysis')
st.title('🦜🔗 WhatsApp Chat Analysis')

st.sidebar.success("Select a demo above.")
# File upload
uploaded_file = st.file_uploader('Upload your chat file', type='txt')
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Run Analysis', disabled=not(uploaded_file))
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

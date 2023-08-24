import streamlit as st
####Importing Necessary Libraries
import re
import pandas as pd
import io
from io import StringIO
import seaborn as sns

# Page title
st.set_page_config(page_title='🦜🔗 WhatsApp Chat Analysis', layout="wide")
st.title('🦜🔗 WhatsApp Chat Analysis')

# creating a single-element container
placeholder = st.empty()

# File upload
uploaded_file = st.file_uploader('Upload your chat file', type='txt')
#with st.form('myform', clear_on_submit=True):
#    submitted = st.form_submit_button('Run Analysis', disabled=not(uploaded_file))

##Parsing whataspp messages to dataframe
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()
    
    whatsapp_regex = r"(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}) - ([^:]*): (.*?)(?=\d{2}/\d{2}/\d{4}, \d{2}:\d{2} - [^:]*|\Z)"
    matches = re.findall(whatsapp_regex, string_data, re.MULTILINE | re.DOTALL)
    df = pd.DataFrame(matches, columns=["date", "time", "name", "message"])
    df['date'] = pd.to_datetime(df['date'],format='%d/%m/%Y')
    df['time'] = pd.to_timedelta(df['time']+':00')
    df['datetime']= df["date"] + df['time']
    df = df.head(10)
    #st.dataframe(df['message'])
    with st.container():
        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("##### ** :red[Most Active Member of the group]**")
            ##Finding pattern of messager
            pattern = re.compile('\d+:\d+\s+-\s+([a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?[a-zA-Z0-9]+\s?):\s+')
            messengers = re.findall(pattern,string_data)
            count_messages={}
            for each in messengers:
                if each in count_messages.keys():
                    count_messages[each]+=1
                else:
                    count_messages[each]=1
            message_cnt = pd.DataFrame.from_dict([count_messages])
        
            message_cnt = message_cnt.T.sort_values(by = 0, ascending=False)
            message_cnt = message_cnt.rename(columns={0: 'Mssg_Count'})
            
            #EDA for general understanding of the distribution of the dataset.
            message_cnt['Names'] = message_cnt.index
            #sns.set(rc={'figure.figsize':(800,600)})
            ax =sns.barplot(x = 'Names', y = 'Mssg_Count' ,data = message_cnt.head(5), estimator = sum, palette=("crest"))
            ax.set_title('Most Active Member of the group', size = 20)
            ax.set(ylabel='No. of Messages')
            st.bar_chart(data = message_cnt.head(5), x = 'Names', y = 'Mssg_Count')
            st.write(ax)
            
        with fig_col2:
            st.markdown("##### Which hour of the day were most messages sent?")
            hour_pattern = '(\d+):\d+\s+-\s+\w+\s?\w+?\s?\w+\s?\w+:\s'
            hours = re.findall(hour_pattern,string_data)
            time = pd.DataFrame({'hours':hours})
            time['count'] = [1]* len(time)
            time = time.sort_values(by = 'hours', ascending = True)
            #EDA for general understanding of the distribution of the dataset.
            st.bar_chart(data = time, x = 'hours', y = 'count')
            st.write(ax)
            
            
            
            

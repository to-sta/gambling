import os
from dotenv import load_dotenv
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import streamlit as st

# Load enviroment variable
load_dotenv()
OPEN_AI_KEY = os.getenv(key='OPEN_AI_KEY')

# Load dataset
df = pd.read_csv('data/ufc_master_data.csv')

# Instantiate a LLM
llm = OpenAI(api_token=OPEN_AI_KEY)
pandas_ai = PandasAI(llm)

# Streamlit App
st.title('Data Analysis Tool with OpenAI Prompt')
st.write('You can use the prompt to ask OpenAI anything about the ufc_master_data set from kaggle')
st.divider()
st.dataframe(df.head(10))

prompt = st.text_area('Here goes your prompt!')

if st.button('Ask OpenAI'):
    with st.spinner(text='Waiting for a response'):
        if prompt:
            st.write(pandas_ai.run(df, prompt=prompt))
            print('was done')
        else: 
            st.warning('Please enter a prompt!')


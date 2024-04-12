import pandas as pd
import streamlit as st
st.info('Site is under construction!.....Please be with me')
df = pd.read_csv('startup_cleaned.csv')

st.sidebar.title('Startup Funding Analysis')

option = st. sidebar.selectbox('Select One', ['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'Startup':
    st.title('Startup Analysis')
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))


elif option == 'Investor':
    st.title('Investor Analysis')
    st.sidebar.selectbox('Select Investor',sorted(df['investors'].unique().tolist()) )
import streamlit as st
st.info('Site is under construction!.....Please be with me')

st.sidebar.title('Startup Funding Analysis')

option = st. sidebar.selectbox('Select One', ['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.title('Startup Analysis')
    st.sidebar.selectbox('Select Startup',['Flipkart','Ola'])
elif option == 'Investor':
    st.title('Investor Analysis')
    st.sidebar.selectbox('Select Investor', ['aamir 1', 'aamir 2'])
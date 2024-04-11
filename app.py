import streamlit as st
st.title ('Startup Dashboard')
st.header('Learning streamlit')
st. write('This is normal text')

col1, col2, col3,col4=st.columns(4)
with col1:
    st.header('Hello')
with col2:
    st.header('World')
with col3:
    st.header('this')
with col4:
    st.header('is Varun')
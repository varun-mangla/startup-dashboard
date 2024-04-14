import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide', page_title='Startup Analysis| Varun Mangla')

#st.info('Site is under construction!.....Please be with me')
df = pd.read_csv('startup_cleaned.csv')

def load_investor_details(investor):
    st.title(investor)

    #load the recent 5 investment of the investor
    last5_df=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
        #Biggest Investments
        big_series= df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig1, ax1 = plt.subplots()
        ax1.bar(big_series.index, big_series.values)
        st.pyplot(fig1)

    with col2:
        #Vertical
        #Round Investments
        round_series= df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('round')
        fig2, ax2 = plt.subplots()
        ax2.bar(round_series.index, round_series.values)
        st.pyplot(fig2)



st.sidebar.title('Startup Funding Analysis')

option = st. sidebar.selectbox('Select One', ['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    st.title('Overall Analysis')

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    st.title('Startup Analysis')


elif option == 'Investor':
    st.title('Investor Analysis')
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)



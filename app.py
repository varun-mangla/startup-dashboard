import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide', page_title='Startup Analysis| Varun Mangla')

#st.info('Site is under construction!.....Please be with me')
df = pd.read_csv('startup_cleaned.csv')
st.subheader("Welcome to Startup Investment Tracker! Explore investments in Indian startups effortlessly")
st.subheader("Select a 'startup' or 'investor' from the sidebar menu or opt for the 'Overall Analysis' for a comprehensive overview")

def load_overall_analysis():
    st.title('Overall Analysis')
    # 1. Total Invested Amount
    total = round(df['amount'].sum())

    # 2. Maximum Amount infused in Startup
    max_funding = round(df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0])

    # 3. Average Funding
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())

    # 4. Total Funded Startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4= st.columns(4)
    with col1:
        st.subheader('Total ')
        st.subheader(str(total) + ' CR')
    with col2:
        st.subheader('Maximum Funding ')
        st.subheader(str(max_funding) + ' CR')
    with col3:
        st.subheader('Average Funding ')
        st.subheader(str(avg_funding) + ' CR')
    with col4:
        st.subheader('Number of Data ')
        st.subheader(str(num_startups) + ' Startups')


def load_investor_details(investor):
    st.title(investor)


    #load the recent 5 investment of the investor
    last5_df=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','round','amount']]
    st.subheader('Recent Investments')
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
        #Type of Investments
        round_series= df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Type of Investment')
        fig2, ax2 = plt.subplots()
        ax2.bar(round_series.index, round_series.values)
        st.pyplot(fig2)

def load_startup_details(startup):
    #Name of startup
    st.title(startup)
    # vertical of startup
    vertical= df[df['startup'].str.contains(startup)]['vertical'].head(1)

    # Sub-vertical of startup
    sub_vertical= df[df['startup'].str.contains(startup)]['subvertical'].head(1)

    # Location of startup
    city= df[df['startup'].str.contains(startup)]['city'].head(1)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Business Vertical: ')
        st.dataframe(vertical)
    with col2:
        st.subheader('Sub-Vertical: ')
        st.dataframe(sub_vertical)
    with col3:
        st.subheader('Location: ')
        st.dataframe(city)

    #load the recent 5 investment of the investor
    investor_df = df[df['startup'].str.contains(startup)].head()[['date', 'investors', 'vertical', 'round', 'amount']]
    st.subheader('Investors')
    st.dataframe(investor_df)

    col1,col2=st.columns(2)
    with col1:
        #Biggest Investors
        big_money = df[df['startup'].str.contains(startup)].groupby('investors')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest Investor')
        fig1, ax1 = plt.subplots()
        ax1.bar(big_money.index, big_money.values)
        st.pyplot(fig1)

    with col2:
        #Type of Investments
        round_series= df[df['startup'].str.contains(startup)].groupby('round')['amount'].sum().sort_values(ascending=False)
        st.subheader('Type of Investment')
        fig2, ax2 = plt.subplots()
        ax2.bar(round_series.index, round_series.values)
        st.pyplot(fig2)

st.sidebar.title('Startup Funding Analysis')

option = st. sidebar.selectbox('Select One', ['Overall Analysis','Startup','Investor'])
if option == 'Overall Analysis':
    btn0= st.sidebar.button('Show Overall Analysis')
    if btn0:
        load_overall_analysis()

elif option == 'Startup':
    st.title('Startup Analysis')
    selected_startup=st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        load_startup_details(selected_startup)

elif option == 'Investor':
    st.title('Investor Analysis')
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)


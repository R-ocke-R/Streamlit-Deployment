import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# '''
# running an error into the pandas read_html method due to wikipedia changing their page structure
# previous code:
# url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
# sp_list = pd.read_html(url) 
# sp_list_500 = sp_list[0]
# ticker_list = list(sp_list_500['Symbol'].values)
# name_list = list(sp_list_500['Security'].values)
# '''

# updated code:
# --- MODIFIED SECTION: Function to scrape S&P 500 data ---
@st.cache_data
def get_sp500_list():
    """Scrapes the list of S&P 500 companies from Wikipedia."""
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'id': 'constituents'})
        df = pd.read_html(str(table))[0]
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to retrieve data from Wikipedia: {e}")
        return pd.DataFrame({'Symbol': [], 'Security': []})

# Load the data
sp_list_500 = get_sp500_list()
ticker_list = list(sp_list_500['Symbol'].values)
name_list = list(sp_list_500['Security'].values)

st.set_page_config(page_title="SPX Market Monitor", page_icon="💹", layout="wide", initial_sidebar_state="collapsed")
st.title("SPX Market Monitor")

with st.expander("About SPX Market Monitor"):
    st.write("""
    SPX Market Monitor allows you to explore the closing prices of companies listed in the S&P 500 index. 
    With an extensive selection of S&P 500 companies, users can easily navigate and select their preferred stocks. 
    Additionally, the site offers customizable date ranges, empowering users to view historical price data 
    based on their specific needs and preferences. Whether tracking market trends or analyzing individual stock 
    performance, SPX Custom Stock Viewer provides an intuitive platform for informed decision-making.
    """)
    st.write("We value your feedback! Please let us know which features would be most helpful to you via connect page.")
    

choice = st.selectbox("The list contains all of the S&P 500 Companies", options = name_list, index = None, placeholder="Please choose a company")

col1, col2 = st.columns(2)
with col1:
    st_default = datetime(2015, 1, 1)
    start = st.date_input("Start Date", value = st_default)

with col2:
    end = st.date_input("End Date")


if(choice!=None):
    selected_index = name_list.index(choice)
    corresponding_ticker = ticker_list[selected_index]
    tickerData = yf.Ticker(corresponding_ticker)
    #get the historical prices for this ticker
    tickerDf = tickerData.history(start=start, end=end)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    st.container(border= False, height=70)
    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)



st.container(border=False, height=200)
st.markdown(
    """
    <footer style="text-align: center; margin-top: 20px;">
        <p style="font-size: 12px; color: #777;">Disclaimer: I don't own the financial stock data. This data is collected by calling yfinance, which is a Python library, based on yahoo finance API.</p>
    </footer>
    """,
    unsafe_allow_html=True
)

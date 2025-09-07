import yfinance as yf
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime


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

st.set_page_config(page_title="Compare S&P 500 stock valuations", page_icon="💸", layout="wide", initial_sidebar_state="collapsed")
st.title("Compare Multiple S&P 500 stock valuations:")

with st.expander("About Compare SP500 Stocks"):
    st.write("""
    Compare SP500 Stocks allows you to compare the closing prices of multiple companies listed in the S&P 500 index. 
    With a vast selection of S&P 500 companies, users can conveniently select and compare the closing prices of 
    multiple stocks on a single graph. This feature enables users to gain insights into relative performance, 
    identify trends, and make informed investment decisions. Additionally, the site offers customizable date ranges, 
    empowering users to analyze historical price data based on their specific needs and preferences.
    """)
    st.write("We value your feedback! Please let us know which features would be most helpful to you via the Connect page.")


stat = False
if stat:
    st.container(border = False, height= 50)

    st.warning("""I've ran into some issue with the yFinance API handling for this website, It will be fixed ASAP! Thanks for visiting.
               Please check out some of my other streamlit works""")

    st.stop()  # App won't run anything after this line

choices = st.multiselect("Select Multiple Companies to compare", options = name_list, default = ['Amazon', 'Apple Inc.', 'Microsoft'])
col1, col2 = st.columns(2)

with col1:
    st_default = datetime(2015, 1, 1)
    start = st.date_input("Start Date", value = st_default)

with col2:
    end = st.date_input("End Date")


if (choices!=None):
    selected_tickers = [ticker_list[name_list.index(option)] for option in choices]
    raw_data = yf.download(selected_tickers, start=start, end=end)
    #st.write("Raw data columns:", raw_data.columns.tolist())

if raw_data.empty:
    st.warning("No data was returned. Please check the tickers or the date range.")
else:
    try:
        # Extract 'Close' prices across tickers
        tickerData = raw_data.xs('Close', axis=1, level=0)
        st.subheader("Closing Price")
        st.line_chart(tickerData)
    except KeyError:
        st.warning("'Close' data not found in the downloaded dataset.")


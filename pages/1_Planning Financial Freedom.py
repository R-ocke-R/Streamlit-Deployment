import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image
import pandas as pd
import time

#--- Path Settings 
# using pathlib to import Path function which helps me keep track of the 
# current directory, making my code resilient/ poratble.
page_title = "Investing"
page_icon = "💹"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
imageEarly = current_dir / "assets" / "PercentEarly10.png"
imageLate = current_dir / "assets" / "PercentLate10.png"
imagetwenty = current_dir / "assets" / "percent20.png"
video = "https://www.youtube.com/watch?v=WEDIj9JBTC8&ab_channel=BigThink"
stdocs = "https://streamlit.io"
currency_symbols = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "INR": "₹"
}

st.set_page_config(page_title=page_title, page_icon=page_icon, layout = "wide", initial_sidebar_state="collapsed")

st.title('Investing 101: Visualizing the Value of Time')

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("Why ?"):
        st.write("""This project is based on a [video](%s) by Big Think. 
                 Where William Ackman introduces finance and investing in under an hour.
                 The video is pretty much a classic and has over 12M views.
                 You can watch the full video or from the 21:30 mark, 
                 where it gets pretty exciting as Ackman highlights the importance of compound interest and 
                 the significant impact of starting early on a person's portfolio
                 (also highlighted in Rule 1 below). """ % video)
with col2:
    with st.expander("How?"):
        st.write("""This interactive web app is built using [Streamlit](%s), a Python library. 
                 Inspired by the investing lecture, I set out to test Streamlit's capabilities by creating this application. 
                 During development, I encountered various challenges, leading me to learn additional Python libraries such as 
                 Pillow for image handling, BeautifulSoup for web scraping, and requests for data retrieval. 
                 I also utilized pathlib to ensure portability and resilience to path changes. 
                 Streamlit provided an ideal platform for translating my idea into a functional and user-friendly interface.""" %stdocs) 
with col3:
    with st.expander("Who is William Ackman?"):
        st.write("Bill Ackman founded and runs Pershing Square Capital Management, a hedge fund with $16 billion in assets under management.")
        st.write("Pershing Square's stock portfolio is concentrated in just seven companies, including Chipotle, Hilton and Google parent Alphabet. ")
        col1, col2, col3 = st.columns([0.3, 2, 2])
        with col2:
            st.metric(label='Net Worth', value = '$4.3B', delta = '-0.57%', help="According to Forbes as of 9/3/24" )
        with col3:
            flink= "https://www.forbes.com/profile/william-ackman/?sh=2a6adb10298d"
            st.link_button("Forbes Link", flink, help="William Ackman")


#RULE 1
# with st.expander("Rule No. 1: Starting Early"):
#     cl1, cl2 = st.columns(2)
#     ie=Image.open(imageEarly)
#     il=Image.open(imageLate)
#     with cl1:
#         st.image(ie, caption = """Investing $10000 dollars at age 22 at 10% rate""")
#     with cl2:
#         st.image(il, caption = 'Investing $10000 dollars at age 32 at 10% rate')

# # Warren 20% Percent
# with st.expander("What if you're warren buffet. 10% Interest Ain't enough for you. right?"):
#     cc,cv,cb = st.columns([1,2,1])
#     i20=Image.open(imagetwenty)
#     with cv :
#         st.image(i20, caption = """Yeah that's 24 million dollars from an original $10000 investment """)

# Here comes the hammer but it has to be very small, just a gist. 
st.subheader("""Calculate and Visualize Potential Investment Growth
        """)
st.write(""" Watching this ⏫ inspiring investing video sparked my interest, I then knew I had to invest but with limited funds
         and just one hour worth of investing knowledge, I turned to Python. 
         Curious about potential returns, I created this app to calculate future earnings based on current investment amount.
         With this tool, you can estimate the value of your investments over time""")

with st.expander("Features", True):
    st.markdown(""" 
            You can change the 4 input box values to fit your investing need, once you are done, click Invest !
            - CurrencyType
            - Amount to Invest
            - Expected Rate %
            - Years to Project
            """)

def compound_money(initial_amount, rate, years):
    """Function to calculate compounded money"""
    compounded_money = []
    current_amount = initial_amount
    
    for year in range(1, years+1):

        current_amount *= (1 + rate / 100)
        compounded_money.append(current_amount)
    
    return compounded_money
def cook():
    """ Gives a toast message and a delay before the calculations appear """
    msg = st.toast('Calculating your portfolio...')
    time.sleep(3)
    msg = st.toast('Please wait while we calculate...')
    time.sleep(3)
    msg.toast("Invested!")
def display():
    """ Calculates and displays year-wise amounts"""
    compounded_values = compound_money(amount, rate, int(years))
    data = {"Year": list(range(1, len(compounded_values)+1)), "Compounded Money": compounded_values}
    df = pd.DataFrame(data)
    global final_amount
    final_amount = df.iloc[-1]['Compounded Money']

    columns = st.columns(5)
    for idx, row in df.iterrows():
        column_idx = idx % len(columns)
        year = int(row['Year'])
        compounded_money = row['Compounded Money']
        percent_increase = ((compounded_money - amount) / amount) * 100
        global currency_symbol
        currency_symbol = currency_symbols.get(currency_type, "$")
        if(idx<10):
            columns[column_idx].metric(f"Year {year}", f"{currency_symbol}{compounded_money:.2f}", f"{percent_increase:.2f}% increase", delta_color="off")
        else:
            columns[column_idx].metric(f"Year {year}", f"{currency_symbol}{compounded_money:.2f}", f"{percent_increase:.2f}% increase")
        time.sleep(0.3)
def notify():
    """ Gives a success message in the end of all the displayed year-wise amounts"""
    if currency_symbol == '$':
        st.success("Your initial investment of USD {:.2f} got converted to USD {:.2f}.".format(amount, final_amount))
    else:
        st.success("Your initial investment of {}{:.2f} got converted to {}{:.2f}.".format(currency_symbol, amount, currency_symbol, final_amount))


# Currency type input
col1, col2, col3, col4, col5= st.columns([7,7,7,7,2])
with col1:
    currency_type = st.selectbox('Select Currency Type', ['USD', 'EUR', 'GBP', 'INR'])
with col2:
    amount = st.number_input(f'Enter Amount in {currency_type}', step=1000, value=5000)
with col3:
    rate = st.number_input("Enter Rate of Increase (%):", min_value=0.0, max_value=100.0, value=10.0)
with col4:
    years = st.number_input("Enter Number of Years:", value = 25)
#with the status symbol, we control the flow of the calculations, which is done via the display function, done only once the user presses invest.
status = False
with col5:
    st.write(" ")
    st.write(" ")
    if st.button('Invest'):
        cook()
        status = True
if (status):
    display()
    notify()

        
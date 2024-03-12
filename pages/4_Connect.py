import streamlit as st
from pathlib import Path
import streamlit_lottie

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "css" / "main.css"

st.set_page_config(page_title="Connect !", page_icon=":mailbox:", layout="wide", initial_sidebar_state="collapsed")

def formsubmitio():
    
    contact_form = """
    <form action="https://formsubmit.co/challenge1consistency@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
   
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(css_file)

def feedback_form():
    st.title("Let's Connect! 🚀")
    st.write("Hello There 👋 ")
    st.write("""Thank you for visiting this website! If you'd like to connect, I've included all of my social media handles on the portfolio page.""")
    st.write("""The pages were crafted using various Python libraries. The core of the web app is powered by Streamlit, a versatile framework for building interactive applications. Other Python Libraries that I've utilized include PILLOW, PathLib, yFinance, and BeautifulSoup, among others.""")
    st.write("""I hope you enjoyed. Don't hesitate to reach out if you have any questions or feedback or if you wanna team up on my next streamlit project.""")

    st.container(border=False, height = 200, )
    st.subheader(":mailbox: Please share any thoughts, ideas, or suggestions you have. 💡")
    formsubmitio()

    # name = st.text_input("Your Name 👤", "")
    # email = st.text_input("Your Email 📧", "")
    # feedback = st.text_area("Your Feedback / Feature Request ✏️", "")

    # if st.button("Submit Feedback"):
    #     if name and email and feedback:
    #         # You can save the feedback to a database or send it via email
    #         st.success("Thank you for your feedback! We'll get back to you soon. 🙌")
    #     else:
    #         st.warning("Oops! It looks like you missed filling out some fields. Please make sure to provide your name, email, and feedback. 🛑")

if __name__ == "__main__":
    col1, col2 = st.columns([4, 2])
    with col1:
        feedback_form()
    with col2:
        with st.container(border=False, height=450):
            st.lottie("https://lottie.host/d5afd3f1-4b92-4cb2-802b-1ed6f0143b65/9VVoumSHNv.json")

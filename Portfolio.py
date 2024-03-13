from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit_lottie
from constants import *


# Page Config
PAGE_TITLE = "Digital CV | Manu Sharma"
PAGE_ICON = "🤖"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


st.markdown("""<style>
  body {
    zoom: 80%;
  }
</style>
""", unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
def hero():
    col1, col2 = st.columns([1,3], gap="small")
    with col1:
        st.image(profile_pic)

    st.markdown("""
        <style>
        .large-text {
            font-size: 4em; 
        }
        </style>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class ="large-text">Manu Sharma</p>', unsafe_allow_html=True)
        st.write(DESCRIPTION)
        st.write(" ")


        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )


def skill_tab(info, skill_col_size):
    st.write('\n')
    st.write('\n')
    st.subheader("Skills:")
    st.write("---")
    rows = len(info['skills']) // skill_col_size
    if len(info['skills']) % skill_col_size != 0:
        rows += 1
    
    skills = iter(info['skills'])
    for row in range(rows):
        columns = st.columns(skill_col_size)
        for column, skill in zip(columns, skills):
            column.button(skill)

     
# --- SOCIAL LINKS ---
def social():
    st.write('\n')
    col_ratios = [1,3,3,3,3]
    cols = st.columns(col_ratios)
    st.write('\n')
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index+1].write(f"[{platform}]({link})")
    

# --- EXPERIENCE & QUALIFICATIONS ---
def experience():
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
    - ✔️ Strong hands on experience and knowledge in Python and Excel
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )



def work():
        
    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Senior Data Analyst | Ross Industries**")
    st.write("02/2020 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**Data Analyst | Chegg**")
    st.write("04/2015 - 01/2018")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )

# --- Projects & Accomplishments ---
def projects():

    st.write('\n')
    st.subheader("Projects")
    st.write("---")
    col1, col2 = st.columns([4, 1.5])
    with col1:
        st.write("📀", "**Streamlit Projects:**")
        st.write("Tech Stack : Python, CSS, Github, VSCode")
        st.write(
            """
        - ► Created a portfolio website.
        - ► Created SPX Market Monitor, an interactive app that allows users to select stocks and customize the timeframe to view stock prices. Upon request, I added a feature that enables users to compare multiple stocks on a single graph.
        - ► View all of my streamlit projects from the sidebar.
        """
        )
        st.write('\n')
        st.write("🤖", "**Machine Learning Projects**")
        st.write("Tech Stack: Python, Jupyter Notebooks")
        st.write(
            """
        - ► Developed a Loan Eligibility Prediction Model, which was enhanced to include a feature ranking mechanism. Leveraging the mRMR technique from my feature selection research, the model provides insights into the main features influencing loan eligibility and highlights potential biases.
        - ► Developed a Smoking Detection Classification Model to identify smoking activity in user-provided images. This project was part of learning CNNs, and their potential applications, Implemented TensorFlow partitions for efficient caching and prefetching of large dataset during training process.
        - ► Waze user churn retention model (Working on this project)
        """
        )
        st.write('\n')
        st.write("📊", "**Tableau Data Visualisations**")
        st.write("Tech Stack: Tableau Public ")
        st.write(
            """
        - ► Analyzing Seoul Transportation Department Dataset, my task was to help optimize bicycle maintenance scheduling by analyzing rented bicycle data collected in 2018. By identifying the time of day with least rental activity, we could ensure minimal disruption to bicycle rental services during standard working hours (8 a.m. to 5 p.m). 
        - ► This project was part of Google Advanced Data Analytics Course, you can read more about the course from the certifications linked above.
        - ► Check out my Tableau Data Dashboard here: https://public.tableau.com/app/profile/manu.sharma.tab/vizzes
        """
        )
    with col2:
        st.lottie("https://lottie.host/f88646a4-f44b-4fff-a7ed-f5f565cb2ca0/lhJFKE6Hld.json")
        st.lottie("https://lottie.host/f839153b-c982-47c6-8b15-c1f600fc751e/UIXYBRQRXW.json")




def education():
    st.write('\n')
    st.subheader("Education:")
    col1, col2 = st.columns([4, 1.5])
    with col1:
        st.write("👨‍🎓", "**Bachelor of Technology | CSE | GLA University, Mathura**")
        st.write("2020 - Present")
        st.write(
            """
        - ► Specialized in AI and ML, completed respective coursework and gained practical experience through project based implementations.
        - ► Coursework: Database Management Systems, Operating Systems, Computer Networks, Data Structures and Algorithms, etc.
        - ► Actively participated in various Hackathons and coding contests.
        - ► GRE (Feb 2024) : Scored 316 : 160 Quant, 156 Verbal.
        - ► CPI : 8.5
        """
        )
        st.write('\n')
        st.write("🏫", "**High School | Science | St. Peter's College, Agra**")
        st.write("2020")
        st.write(
            """
        - ► Choose PCM + Computer Science as my High School Subjects and got an aggregate of 91%.
        - ► Guided a team of 20 students as an event head of a mobile gaming contest, at a state level technical fest (Techno-Fi, 2020) .
        - ► Successfully managed academic responsibilities while nurturing my passion for football and athletics.
        """
        )
    with col2:
        st.lottie("https://lottie.host/bbc58d2e-9eaf-4c8c-8354-f98977e8cc19/qpzkCwQW6I.json")


def research():
    st.write('\n')
    st.subheader("Research Work:")
    st.write("---")
    col1, col2=st.columns([5, 1])

    with col1:
            
        st.write("📄", "**Optimising Feature Selection: A Comparative Study of mRMR-Boruta/RFE Hybrid Approach**")
        st.write("March 2023")
        st.write(
            """
        - ► Contributed to a research in Machine Learning: Data Mining Domain
        - ► Proposed a hybrid feature selection model combining mRMR and Boruta/RFE to enhance data preprocessing
        - ► Using the novel approach, classification accuracy was increased from 90.21% using earlier techniques to 95.83%
        - ► Worked under the guidance of Prof. Dilip Kumar Sharma, Dean (International Relations) GLA University.
        - ► The paper was accepted for publication in the ISCON 2023 conference. Link.
        - ► https://ieeexplore.ieee.org/document/10112125
        """
        )
    with col2:
        st.lottie("https://lottie.host/5cb583ed-32c0-4b0b-b548-d7a78775fb61/TAT6FCn5q3.json")


def scores():
    st.write('\n')
    st.subheader("Certifications & Scores:")
    st.write("---")
    col1, col2, col3  = st.columns([2.5,1.5,1])
    with col1:

        st.write("Certifications:")
        for project, link in Certtifications.items():
            st.write(f"[{project}]({link})")
    with col2:
        st.write("Hackerrank Skills:")
        for project, link in HackerrankSkillBadged.items():
            st.write(f"[{project}]({link})")
    with col3:
        st.write("CP & Leetcode Profiles:")
        for project, link in cp.items():
            st.write(f"[{project}]({link})")


hero()
with st.container(border=True, height=90):
    social()
st.container(border=False, height=40)
education()
skill_tab(info, skill_col_size)
research()
scores()


    
projects()
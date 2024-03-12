from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit_lottie
from constants import *


# Page Config
PAGE_TITLE = "Digital CV | Manu Sharma"
PAGE_ICON = "🤖"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="collapsed")


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
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")


def education():
    st.write('\n')
    st.subheader("Education:")
    col1, col2 = st.columns([4, 1.5])
    with col1:
        st.write("👨‍🎓", "**Bachelor of Technology | CSE**")
        st.write("2020 - Present")
        st.write(
            """
        - ► Specialized in AI and ML, completed respective coursework and gained practical experience through project based implementations.
        - ► Coursework: Database Management Systems, Operating Systems, Computer Networks, Data Structures and Algorithms, etc.
        - ► Actively participated in various Hackathons and coding contests.
        - ► CPI : 8.5
        """
        )
        st.write('\n')
        st.write("🏫", "**High School | Science**")
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


    # Displaying bachelor's degree information in the first column
    # with col1:
    #     st.subheader("Bachelors")
    #     st.write(f"- **Degree:** {bachelors_info['degree']}")
    #     st.write(f"- **Field of Study:** {bachelors_info['field_of_study']}")
    #     st.write(f"- **University:** {bachelors_info['university']}")
    #     st.write(f"- **Year:** {bachelors_info['year']}")

    # # Displaying high school information in the second column with a bigger font size
    # with col2:
    #     st.write("**High School**")
    #     st.markdown(f"## {high_school_info['school']}")
    #     st.write(f"- **Year:** {high_school_info['year']}")


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




hero()
with st.container(border=True, height=90):
    social()
st.container(border=False, height=40)
education()
skill_tab(info, skill_col_size)
research()



    
projects()
from pathlib import Path

# --- Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume Manu Sharma.pdf"
profile_pic = current_dir / "assets" / "profile-pic-b.png"



# Description
DESCRIPTION = """
As a recent CS graduate I am eager to embark on my professional journey.
With a strong foundation in programming and a passion for problem solving, 
I am enthusiastically pursuing opportunities in both **software development engineering** and **data science**. 
Whether it's crafting elegant code to build robust applications or delving into complex data analysis to derive actionable insights, I am open to starting my career in either role.
"""


# Media links
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/manu-sharma229/",
    "GitHub": "https://github.com/r-ocke-r",
    "Twitter": "https://twitter.com/Manusharma79105",
    "Leetcode": "https://leetcode.com/r_ocke_r"
}

# Platform links
platform_icons = {
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
    "GitHub": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    "Twitter": "https://cdn-icons-png.flaticon.com/512/124/124021.png",
    "Leetcode": "https://assets.leetcode.com/static_assets/public/icons/favicon.ico"
}

info = {'skills': ['Python', 'Java', 'Machine Learning', 'Streamlit', 'Data Analysis', 'SQL', 'PopSQL', 'Jupyter Notebooks', 'Tableau', 'Excel', 'Web Scraping','HTML', 'CSS']}

skill_col_size = 4



# Display education information


bachelors_info = {
    'degree': 'Bachelor of Technology',
    'field_of_study': 'Computer Science Engineering',
    'university': 'GLA University, Mathura',
    'year': "2020-2024"
}

high_school_info = {
    'school': "St. Peter's College, Agra",
    'year': 2018
}


Certtifications = {
    "🏅 Python 3 Programming Specialization by University of Michigan, on coursera": "https://www.coursera.org/specializations/python-3-programming",
    "🏅 Google Advanced Data Analytics Professional Certificate": "https://www.coursera.org/professional-certificates/google-advanced-data-analytics",
}

HackerrankSkillBadged = {
    "🥇 Problem Solving 5 Star Badge" :"https://www.hackerrank.com/profile/r_ocke_r",
    "📟 Problem Solving Assessment" : "https://www.hackerrank.com/certificates/2e4e60c95340",
    "🥇 Python 5 Star Badge" : "https://www.hackerrank.com/profile/r_ocke_r",
    "🥈 SQL 5 Star Badge" :"https://www.hackerrank.com/profile/r_ocke_r",
    "🥉 C 2 Star Badge" :"https://www.hackerrank.com/profile/r_ocke_r" 
}

cp={
    "Leetcode 250+ " : "https://leetcode.com/r_ocke_r",
    "Codechef 1556 rating" : "https://www.codechef.com/users/r_ocke_r"
}


PROJECTS = {
    "🏆 Compare S&P Stocks - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
}
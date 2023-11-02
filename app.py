from pathlib import Path

import streamlit as st
from PIL import Image

#  python -m streamlit run app.py

# ---- PATH SETTINGS ---- #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Whyte, Tavion Resume 10-31-23.pdf"
cv_file = current_dir/"assets"/"Whyte, Tavion 10-31-23 CV.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"

# ---- GENERAL SETTINGS ---- #
PAGE_TITLE = "Digital CV | Tavion Whyte"
PAGE_ICON = "👨‍💻"
NAME = "Tavion Whyte"
DESCRIPTION = """
QA Analyst / Software Engineer \n# Assisting enterprises by suppporting data-driven decision making. 
"""
EMAIL = "Whyte.T@tcs.com | TayyWhyte@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn 🟦": "https://www.linkedin.com/in/tavion-whyte-3842a118b/",
    "Github 🟢": "https://github.com/tayyglo",
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# ---- LOAD CSS, PDF, & PROFILE PIC ---- #
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(cv_file, "rb") as pdf_file2:
    PDFbyte2 = pdf_file2.read()
profile_pic = Image.open(profile_pic)

# ---- HERO SECTION ---- #
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=320)
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label="📄 Download CV",
        data=PDFbyte2,
        file_name=cv_file.name,
        mime="application/octet-stream",
    )
    st.write("📬",EMAIL)
    
# ---- SOCIAL LINKS ---- #
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# ---- EXPERIENCE & QUALIFICATIONS ---- #
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """ 
    ✅ Hands on experience and knowledge in test automation and Java
    \n✅ Good understanding of testing principles and their respective applications
    \n✅ Excellent team-player, displaying strong sense of initative on tasks
    """
)

# ---- SKILLS ---- #
st.write("#")
st.subheader("Hard Skills")
st.write(
    """ 
    - Test Automation: Java Selenium, Rest Assured, codeless automation tools (Accelq, Katalon) 
    - Manual Testing: API testing using Postman, SoapUI
    - Programming: Java, Angular, JavaScript/p5.js, HTML, MS Office, 
        minor exposure to Python, C++, PHP, Scheme, PureData
    - Databases: MongoDb, MySQL
    """
)
st.write("#")
st.subheader("Soft Skills")
st.write(
    """ 
    - Public speaking, leadership, and organizational skills
    - Intercultural competence and cross-cultural communication skills
    - Team building, creative thinking, time management, and project management skills 
    """
)

# ---- WORK HISTORY ---- #
st.write("#")
st.subheader("Work History")
st.write("---")

# ---- JOB 1
st.write("Tool Administrator")
st.write("*", "**October 2022 | September 2023**")
st.write(
    """
    - > Defined resolutions to bugs and trouble tickets for automated test tool with 91% conclusion rate
    - > Maintained status and provided updates for active and inactive VM/ remote agents
    - > Facilitated user access database for testing tool ensuring uninterrupted service

    """
)
st.write("#")
# ---- JOB 2
st.write("QA Analyst")
st.write("*", "**March 2022 | October 2022**")
st.write(
    """
    - > Led a team of two offshore analyst to generate and manage test suites for internal applications
    - > Manual and Automated API testing working with selenium-based code free platform
    - > Implementing Agile methodology, overseeing quality of revisions providing continuous test support to dev team
    - > Developed over fifty resources, wikis, or artifacts to successfully facilitate transition of knowledge to other resources

    """
)
st.write("#")
# ---- JOB 3
st.write("ILP Onboarding")
st.write("*", "**August 2021 | October 2021**")
st.write(
    """
    - > Phase One: Core Java Training 
    - > Phase Two: MEAN Stack training

    """
)
st.write("#")

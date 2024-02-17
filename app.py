# Import necessary libraries
from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "ResumeVersion6.pdf"
profile_pic_path = current_dir / "assets" / "images" / "Headshot_modified.png"
ui_technology = current_dir / "assets" / "images" / "ui.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pradyumna A Kubear"
PAGE_ICON = ":wave:"
NAME = "Pradyumna Anil Kumar Kubear"
DESCRIPTION = """
Web developer and an Aspiring Data Science Enthusiast
"""
EMAIL = "pradyumkubeara@gmail.com"
SOCIAL_MEDIA = {
    "Email": "pradyumkubeara@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/pradyumna-anil-kumar-kubear-592866172/",
    "GitHub": "https://github.com/PradyumnaA",
}
PROJECTS = {
    "🏆 Twitter Sentiment Analysis":"https://github.com/PradyumnaA/TwitterSentimentAnalysis",
    "🏆 Beauty Product Recommendation System":"https://github.com/PradyumnaA/BeautyProductRecommendationSystemUsingPython",
    "🏆 Indian Delicacies":"https://indiandelicacies-stockton.web.app/",
    "🏆 Maze Project":"https://github.com/PradyumnaA/MazeProblem",
    "🏆 Perceptron And CNN":"https://github.com/PradyumnaA/PerceptronAndCNN",
    "🏆 Markov Distribution Program":"https://github.com/PradyumnaA/Markov-Distribution-Program",
    "🏆 Hospital Management System Using Tkinter":"https://github.com/PradyumnaA/HospitalManagementSystem",
    "🏆 Drumkit Project":"https://github.com/PradyumnaA/DrumKit_1",
    "🏆Medibot Project":"https://github.com/PradyumnaA/medibot"
    
    
}


# Defining configuration for Streamlit
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Load PDF
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# Load profile picture
profile_pic = Image.open(profile_pic_path)
ui_technologies_image = Image.open(ui_technology)

# Hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=190)

with col2:
    st.write(f"# {NAME}")
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",  # unknown binary file
    )
    st.write("📫", EMAIL)

# --Social Links--#
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience and qualifications
st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
- ✔️ 2 Years experience with web development and mobile app development
- ✔️ 1 Year experience as a data science tutor at the University of the Pacific
- ✔️ Helped in solving errors related to Python programming
- ✔️ Worked on Tkinter Interface
"""
)

# Skills
st.write("#")
st.subheader("Skills")
st.write("""
- 👨‍💻 Programming Languages: 🐍 Python, ☕ Java Script
- 📐 Technologies: ⚛️ReactJS, 🔥 Firebase,📱React Native
- UI Skills: Figma, Proto pie, Canva
- Other Software: Android Studio, Web Strom, Visual Studio Code, Import-IO, MS Word, Power Point, Excel

""")
# Projects and Accomplishments
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

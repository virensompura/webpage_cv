import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Viren-CV", page_icon="📄", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


#lottie Animation
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dxnyiaap.json")
lottie_coding_1 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_vq5wzcvx.json")
lottie_coding_2 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_efbizstn.json")


#Header Section
with st.container():
    st.subheader("Hi, I am Viren Sompura :wave:")
    st.title("Robotics Engineer From India 🇮🇳")
    st.write("Seeking great opportunities where I can utilize my skills and simultaneously learn new technologies to contribute towards organization’s growth")

#what are my skills
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Skills")
        st.subheader("Python")
        progress_value = 50 / 100  # Set the progress value to 50
        skill1_levels = ["Beginner", "Intermediate", "Advanced"]
        st.progress(progress_value)
        st.write(f"Python Level: {skill1_levels[int(progress_value * 2)]}")

        # Skill 2
        st.subheader("CATIA V5")
        progress_value_2 = 80 / 100  # Set the progress value to 50
        skill2_levels = ["Beginner", "Intermediate", "Advanced"]
        st.progress(progress_value_2)
        st.write(f"CATIA V5 Level: {skill2_levels[int(progress_value_2 * 2)]}")

        st.subheader("Automation Studio")
        progress_value_3 = 100 / 100  # Set the progress value to 50
        skill3_levels = ["Beginner", "Intermediate", "Advanced"]
        st.progress(progress_value_3)
        st.write(f"Automation Studio Level: {skill3_levels[int(progress_value_3 * 2)]}")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        st_lottie(lottie_coding_2, height=300, key="coding_2")

#Education
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding_1, height=300, key="coding_1")
    with right_column:
        st.header("Education")
        st.subheader("Sal College of Enginnering, B. Tech Mechatronics, 2020")
        st.metric(label="CGPA", value="8.02")
        st.write("Description of your education.")

        st.subheader("M.S. Ramaiah University of Applied Science, M. Tech Robotics Engineering, Present")
        st.metric(label="CGPA", value="9.02")
        st.write("Description of your education.")
        

#Contact Me
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/sompuraviren03@gmail.com" method="POST">
     <input type="hidden" name="_captca" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

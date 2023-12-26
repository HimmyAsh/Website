from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


# --Assets--
lottie_coding = load_lottieurl("https://lottie.host/bee10533-a107-4f07-83b9-8d2f6465ca9e/B1TuOwJoL3.json")
img_ReverseShell = Image.open("Images/ReverseShell.png")
img_test = Image.open("Images/test.png")

# --Header-- 
with st.container():
    st.subheader("Hello, I am Cameron :wave:")
    st.title("A cybersecurity/It specialist")
    st.write("I have a keen passion for the Cybersecurity field. I enjoy creating fun and interesting projects")
    st.write("[My Projects](https://github.com/HimmyAsh)")

# -- About Himmy --
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            I'm creating this website as a portfolio project webpage.
            - I am 23 years old and have been working in the IT field for roughly 3 years now.
            - I enjoy learning and creating cool projects. 
            - My goal is to be able to show others how I got going in the IT field.
            """
        )
        st.write("[Socials]()")
    with right_column:
        st_lottie(lottie_coding, height=300, key="cyber")

# -- Projects ---
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ReverseShell)
    with text_column: 
        st.subheader("Creating a reverse shell into any windows machine")
        st.write(
            """
            In this project we will be creating a reverse shell to remotely access any windows machine.
            I don't codone this behavior in any malicious ways. This is for educational purposes only.
            """
        )   
        st.markdown("[Windows Reverse Shell](https://github.com/HimmyAsh/HimmyAsh)")

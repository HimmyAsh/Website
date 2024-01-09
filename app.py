import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit.components.v1 as components



##Hiding fullscreen options
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

#Defining lottier
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

# --Assets--
lottie_coding = load_lottieurl("https://lottie.host/bee10533-a107-4f07-83b9-8d2f6465ca9e/B1TuOwJoL3.json")
img_ReverseShell = Image.open("Images/ReverseShell.png")
img_test = Image.open("Images/test.png")
lottie_coding2 = load_lottieurl("https://lottie.host/90982730-c7c4-481e-9496-0bfc9da546c4/g18iuZrJjF.json")
Himmy_Ash1 = Image.open("Images/Icon.png")
Himmy_Ash2 = Image.open("Images/LogoWhiteTxt.png")



st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
initial_sidebar_state=st.session_state.get('sidebar_state', 'expanded')
st.write("##")



def run():
    iframe_src = "https://github.com/HimmyAsh"
    components.iframe(iframe_src)
   # You can add height and width to the component of course.

if __name__ == "__main__":
    run()



#adjusting the page size
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)




# Using local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("styles/style.css")


# --Header-- 
header_container = st.container()
with header_container:
    st.write("---")
    header_column, logo_column = st.columns([3, 1])  # Adjust the column ratios as needed
    with header_column:
        st.write("Hello, I am Cameron :wave:")
        st.title("A cybersecurity/IT specialist")
        st.write("I have a keen passion for the Cybersecurity field. I enjoy creating fun and interesting projects")
        st.write("[My Projects](https://github.com/HimmyAsh)")
    with logo_column:
        st.image(Himmy_Ash1, width=125)





# side bar image
st.sidebar.image(Himmy_Ash2, width=150)
# Changing the sidebar color
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #333;  /* Set your desired background color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

#Sidebar
with st.sidebar:
    st.write("---")
    st.markdown("<span style='color:white; font-weight:bold; font-size:30px;'>Welcome!</span>", unsafe_allow_html=True)
    st.write("[<span style='color:white; font-weight:bold;'>About me</span>](https://himmyash.streamlit.app/~/+/#about-me)", unsafe_allow_html=True)
    st.write("[<span style='color:white; font-weight:bold;'>My Projects</span>](https://himmyash.streamlit.app/~/+/#My-Projects)", unsafe_allow_html=True)
    st.write("[<span style='color:white; font-weight:bold;'>GitHub</span>](https://github.com/HimmyAsh)", unsafe_allow_html=True)




        
    
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
        st_lottie(lottie_coding, height=200, key="cyber")
        
# Adding custom CSS to adjust About Himmy
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 4rem;
                }
        </style>
        """, unsafe_allow_html=True)

   # st.write("[Socials]()")
    #with right_column:
      #  st_lottie(lottie_coding, height=200, key="cyber")

# -- Projects ---
with st.container():
    st.write("---")
    st.header("My projects")
# -- Columns are labed by [#] -- 
    project_column = st.columns(2)
    with project_column[0]:  # text_column
        st.write("Creating a reverse shell into any windows machine")
        st.write(
            """
            In this project, we will be creating a reverse shell to remotely access any windows machine.
            I don't condone this behavior in any malicious ways. This is for educational purposes only.
            """
        )   
        st.markdown("[Windows Reverse Shell](https://github.com/HimmyAsh/HimmyAsh)")

    #with project_column[1]:  # image_column
        #st.image(img_ReverseShell, width=225)


# Connect with me section
with st.container():
    st.write("---")
    st.header("Connect with me")
    
    Connect_column = st.columns(1)
    
    with Connect_column[0]:
        st.write("Want to connect with me? Here are my socials!")
        st.write(
            """
            This is a test section for the time being. This project is still in development.
            """
        )


# Contact Me section
with st.container():
    st.write("---")
    st.header("Contact Me")
    
    # formsubmit.co 
    contact_me = """
    <form action="https://formsubmit.co/cma.servers@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Email Address" required>
     <input type="message" placeholder="Message" required>
     <button type="submit">Send</button>
    </form>
    """
    
    Contact_Column = st.columns(2)
    
    with Contact_Column[0]:
        st.markdown(contact_me, unsafe_allow_html=True)
        
    with Contact_Column[1]:
        st.image(Himmy_Ash2, width=300)





    with Contact_Column[1]:
        st.image(Himmy_Ash2, width=300)

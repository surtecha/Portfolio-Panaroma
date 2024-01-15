import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Suryateja | Devfolio", page_icon="🧑🏻‍💻", layout="wide")

# Load CSS
css_file = "styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Assets
lottie_gif = load_lottie_url("https://lottie.host/fbedf2e2-0a44-4c8c-abd4-ec8377be7bb7/3aLPCg9I1W.json")
cocktail = load_lottie_url("https://lottie.host/2407930d-41c8-447f-ac6e-470897603bb1/TjrxJF0uGW.json")
passion = load_lottie_url("https://lottie.host/02be80b8-cfbc-454d-b79a-dc5f6cfa3367/a5BMgdIUWt.json")
hack = load_lottie_url("https://lottie.host/3a4fc800-ca4d-4d0b-a5aa-e094f6c39f2b/Ro4wYU0Tvb.json")
graph = load_lottie_url("https://lottie.host/b9b39243-43f2-42fd-acb9-b65ad93e49e4/URUlBtR9jo.json")
soon = load_lottie_url("https://lottie.host/ed1f42d6-e602-4031-ae82-e5a0d3c37797/93yWIWub4Z.json")
book = load_lottie_url("https://lottie.host/399eeb47-f907-41ff-b741-6df3b88f19e3/OmoDhahUpN.json")
oss = load_lottie_url("https://lottie.host/f0339fdd-342f-4813-aa3e-2bba2af60a90/r9g9k8pYc8.json")

profile = Image.open("assets/profile.png")

conf2 = Image.open("assets/IEEE2.jpg")
conf4 = Image.open("assets/IEEE4.jpg")

ws1 = Image.open("assets/ws1.jpg")
ws2 = Image.open("assets/ws2.jpg")
ws3 = Image.open("assets/ws3.jpg")
ws4 = Image.open("assets/ws3test.jpg")
ws5 = Image.open("assets/ws4.jpg")
ws6 = Image.open("assets/ws5.jpg")

teach1 = Image.open("assets/Teach1.png")
teach2 = Image.open("assets/Teach2.png")

holopin = Image.open("assets/holopin.png")

coming_soon = Image.open("assets/giphy.gif")
kmeans = Image.open("assets/kmeans.PNG")


# Header
with st.container():
    info_column, img_column = st.columns((3, 1))
    with info_column:
        st.title("SURYATEJA CHALLA")
        st.markdown("##### Comp Sci Undergrad • Academic Researcher • ML Fanatic")
        st.write("##")
        linkedin, github = st.columns(2)
        with linkedin:
            st.subheader("[LinkedIn](https://linkedin.com/in/suryatejachalla)")
        with github:
            st.subheader("[Github](https://github.com/surtecha)")
    with img_column:
        st.image(profile)


# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns((3, 1.5))
    with left_column:
        st.title("Nice to meet you!")
        st.markdown("#### I'm Suryateja :wave:")
        st.markdown(
            """
            - ###### 💠 Third year undergraduate in Computer Science 💻
            - ###### 💠 I do competitive programming as a hobby and a sport 👨‍💻
            - ###### 💠 Academic research is my intellectual playground 🔬
            - ###### 💠 Nothing steals my attention more than a new Deep Learning model 🤖
            - ###### 💠 I love to play badminton 🏸 and occasionally play volleyball 🏐
            """
        )
    with right_column:
        st_lottie(lottie_gif, width=300, key="ML")

# Research work
with st.container():
    st.write("---")
    st.title("Research is Fun")
    content, gif_section = st.columns((10, 1))
    with content:
        st.write(
            """
            *Interdisciplinary research is similar to crafting a flavorful cocktail, where the infusion of diverse 
            topics adds a distinct and intriguing twist to the mix.*
            """)
        st.subheader("International Conference")
    with gif_section:
        st_lottie(cocktail, key="cocktail")

    st.markdown("##### [\"An Early Recommendation Tool to Enhance Medicinal Plant Growth based on GIS and Soil Data\"]"
                "(https://doi.org/10.1109/IC2E357697.2023.10262541)")

    st.write(
        """
        An innovative early-stage machine learning-driven recommendation tool, utilizing GIS data to pinpoint ideal 
        geolocations and soil conditions for the revival of endangered medicinal herbs. 
        """
    )

    st.write(
        """
        We authored a paper on this innovative approach, which was one of the **305** selected out of over **1000** 
        submissions for presentation originating from **8** countries, at the prestigious *IEEE International Conference 
        on Computer, Electronics and Electrical Engineering And Their Applications (IC2E3-2023)*, hosted by the National 
        Institute of Technology, Uttarakhand, India.
        """
    )

    st.markdown("##### I was extended an invitation to present our research, and coincidentally, I was the youngest presenter at the conference 🎉")

    left, right = st.columns((3, 2))
    with left:
        st.image(conf2)
    with right:
        st.image(conf4, width=328)

    st.write("##")
    st.header("Project GeoHerb")
    st.markdown("##### This paper is currently under review")
    st.write("""
        An extension to our work on conservation of medicinal herbs. The project utilized a choropleth-based 
        visualization technique to determine the most well-suited geographic location to repopulate vulnerable medicinal 
        herbs.
    """)
    st.markdown("##### The proposed system has a state-of-the-art classification accuracy of **98.7%**")
    st_lottie(soon, width=180, key="coming_soon")


# Extra curricular activities
with st.container():
    st.write("---")
    st.title("Passions That Drive Me")
    gif_section, content = st.columns((1.5, 10))
    with gif_section:
        st_lottie(passion, key="passion")

    with content:
        st.write(
            """
            *Each extracurricular activity I embrace brings an unexpected and exciting plot twist to the storyline of
             my life outside the classroom.*
            """
        )
        st.subheader("Sharing Knowledge is Fun")

    st.write(
        """
        Whether leading our institute's Cybersecurity club - *Aegis* or as a co-founder of the competitive 
        programming club - *Algoholics*, my journey through these pursuits has been an incredible avenue for 
        sharing knowledge and expertise with fellow students and guiding juniors along the way. 
        """
    )
    left, right = st.columns((9, 1))
    with right:
        st_lottie(hack)
    with left:
        st.subheader("Hacking the Wifi Password is interesting 🐱‍💻")
    image, content = st.columns((1, 2))
    with image:
        st.image(ws1)
    with content:
        st.write(
            """
                I demonstrated the captivating process of cracking a wireless LAN password, delving into the realm of 
                brute-force attacks to expose the vulnerabilities lurking within feeble passcodes, all while harnessing 
                the power of **Kali Linux** with a dash of technological finesse. 
            """
        )
        st.markdown("##### The workshop saw an outstanding turnout, with more than **120** students in attendance.")
        st.markdown("#### The highlight? I cracked the Wi-Fi password of our own institute with a "
                    "brute-force attack 😅 😂")
    img1, img2, img3 = st.columns(3)
    with img1:
        st.image(ws2)
    with img2:
        st.image(ws3)
    with img3:
        st.image(ws4)
    st.markdown("#### PS: I was permitted to hack the password for demonstration purposes.")

    st.write("##")
    col1, col2 = st.columns((1, 10))
    with col1:
        st_lottie(graph)
    with col2:
        st.subheader("Teaching others has been a joyride")
    st.write(
        """
        From unraveling the intricacies of graph theory to demystifying the nuances of multi-threaded systems, my 
        passion for teaching and knowledge sharing has always been my guiding principle.
        """
    )
    text, gif= st.columns((8, 1))
    with text:
        st.markdown("#### *\"If you want to master something, teach it. The more you teach, the better you learn.*\"")
        st.markdown("##### - Prof. Richard Feynman")
    with gif:
        st_lottie(book)
    left, right = st.columns(2)
    with left:
        st.image(teach2)
    with right:
        st.image(teach1)
    st.write("##")
    content, gif = st.columns((10, 2))
    with gif:
        st_lottie(oss)
        st.write("[My Holopin board](https://www.holopin.io/@suryatejachalla#)")
    with content:
        st.subheader("Open-source Odyssey: **Hacktoberfest**")
        st.image(holopin)


# Interactive Projects Section
with st.container():
    st.write("---")
    st.title("I'm Working on... 🚀")

    # Creating Tabs for Each Project
    project1, project2, project3 = st.tabs(["GeoHerb", "SignLangNET", "ClusterCraft"])

    with project1:
        st.header("GeoHerb")

        col1, col2 = st.columns([2, 1])  

        with col1:
            st.write(
                """
                - 🔹 Utilizes geospatial and soil data along with ML algorithms to find optimal medicinal herb growth location.
                - 🔹 QGIS is the software used to perform feature extraction on the geospatial vector files.
                - 🔹 GeoPandas and Fiona are major Python libraries used in handling the geo-data.
                - 🔹 Decision tree-based models are implemented for effective classification of soil and regions.
                - 🔹 An impressive classification accuracy of 98.7% has been achieved.
                """
            )
            st.markdown("#### The project will be made open-source after the paper is published.")
        
        with col2:
            # Using the provided GIF URL
            st.image("https://i.giphy.com/media/oFDSjMfe11iiOgQRfY/giphy.webp", width=300)

    st.write("##")  # Space before next project



    with project2:
        st.header("SignLangNET")
        st.write(
            """
            - 🔹 A system that can instantly recognize sign language gestures, making communication more accessible.
            - 🔹 OpenCV, a powerful computer vision library, is used to capture and process a live gestures video feed.
            - 🔹 TensorFlow, a machine learning framework, is employed to train and fine-tune a neural network model.
            - 🔹 Transfer learning with MobileNet SSD for efficient sign language recognition.
            """
        )
        progress = 75  # Static progress value
        st.progress(progress)
        st.write(f"Development Progress: {progress}%")
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTVicGRwYnhqMWlzNjlvNW16ZGY5aGliNjUycWl1NXRsazF0bmpkeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/TLeLKUdIc1tvAxb7ab/giphy.gif", width=300)

    with project3:
        st.header("ClusterCraft")

        col1, col2 = st.columns([2, 1])  

        with col1:
            st.write(
                """
                - 🔹 Implemented k-Means algorithm for image clustering from scratch.
                - 🔹 The project is deployed on a Flask web-app.
                - 🔹 Allows users to upload an image and select the number of clusters.
                - 🔹 Attracted 3 contributors during Hacktoberfest.
                """
            )
            st.markdown("[View ClusterCraft on GitHub](https://github.com/surtecha/ClusterCraft)", unsafe_allow_html=True)

        with col2:
            st.image(kmeans, caption='Image clustering using k-Means algorithm')

        st.write("##") 


st.write("##")
st.write("Last updated: 15 Jan, 2024")
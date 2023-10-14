import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Suryateja | Devfolio", page_icon=":tada:", layout="wide")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Assets
lottie_gif = load_lottie_url("https://lottie.host/fbedf2e2-0a44-4c8c-abd4-ec8377be7bb7/3aLPCg9I1W.json")
cocktail = load_lottie_url("https://lottie.host/2407930d-41c8-447f-ac6e-470897603bb1/TjrxJF0uGW.json")
passion = load_lottie_url("https://lottie.host/02be80b8-cfbc-454d-b79a-dc5f6cfa3367/a5BMgdIUWt.json")

soon = load_lottie_url("https://lottie.host/ed1f42d6-e602-4031-ae82-e5a0d3c37797/93yWIWub4Z.json")

test_img = Image.open("assets/test.png")
conf1 = Image.open("assets/IEEE1.jpg")
conf2 = Image.open("assets/IEEE2.jpg")
conf3 = Image.open("assets/IEEE3.jpg")
conf4 = Image.open("assets/IEEE4.jpg")


# Header
with st.container():
    info_column, img_column = st.columns((3, 1))
    with info_column:
        st.title("SURYATEJA CHALLA")
        st.subheader("Comp Sci Undergrad | M.L. researcher")
        linkedin, github, mail = st.columns(3)
        with linkedin:
            st.write("[LinkedIn](https://linkedin.com/in/suryatejachalla)")
        with github:
            st.write("[Github](https://github.com/in/suryateja-challa)")
        with mail:
            st.write("[Mail](mailto:challasuryateja29@gmail.com)")
    with img_column:
        st.image(test_img, width=200)


# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns((3, 1.5))
    with left_column:
        st.title("Nice to meet you!")
        st.markdown("#### I'm Suryateja :wave:")
        st.markdown(
            """
            - ##### 💠 Second year undergraduate in Computer Science 💻
            - ##### 💠 I do competitive programming as a hobby and a sport 👨‍💻
            - ##### 💠 Academic research is my intellectual playground 🔬
            - ##### 💠 Nothing steals my attention more than a new Deep Learning model 🤖
            - ##### 💠 I love to play badminton 🏸 and occasionally play volleyball 🏐
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
        submissions originating from **8** countries, at the prestigious IEEE International Conference on Computer, 
        Electronics and Electrical Engineering And Their Applications (IC2E3-2023), hosted by the National Institute of 
        Technology, Uttarakhand, India.
        """
    )

    st.write(
        """
        I was extended an invitation to present our research, and coincidentally, I was the youngest presenter at the 
        conference 🎉
        """
    )

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
    st_lottie(soon, width=180,key="coming_soon")



# Extra curricular activities
with st.container():
    st.write("---")
    st.title("Passions That Drive Me")
    gif_section, content = st.columns((1.5, 10))
    with gif_section:
        st_lottie(passion, key="passion")

    with content:
        st.markdown("### ```if(dreams && action): future='limitless'```")
        st.markdown("### ```else: life='static'```")
        st.write("##")
        st.subheader("Sharing Knowledge is Fun")

    st.write("The best part of giving knowledge")


# Projects
with st.container():
    st.write("---")
    st.header("Passions Projects in Focus")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(test_img)
    with text_column:
        st.subheader("GeoHerb")
        st.write(
            """
            - Uses that
            - Does this
            - You get it
            """
        )
        st.markdown("[Check out the project](https://www.google.com)")

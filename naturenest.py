"""
# My first app
Here's our first attempt at using data to create a table:
"""

from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium, folium_static
from PIL import Image
import PIL.Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from folium import Choropleth
import time
from streamlit_chat import message
from streamlit.components.v1 import html
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


st.set_page_config(
    page_title="Nature Nest",
    layout="centered",
    initial_sidebar_state="expanded"
)


image = Image.open('/Users/monish/Documents/naturenest profile picture.png')
st.image(image, caption='', width=700)


# import folium

selected2 = option_menu("", ["Home", "Events", "Purdue", "Discuss", "Profile"],
                        icons=['house', 'calendar-event',
                               "building", 'chat', 'person-circle'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# Events


def show_event_page():
    selected2 = "Events"


if selected2 == "Events":

    st.subheader('Host an Environmental Event!')
    with st.form(key='myform', clear_on_submit=True):
        title = st.text_input("Event Title:")
        date = st.text_input("Enter the Date:")
        organizer = st.text_input("Enter the Organizer:")
        description = st.text_area("Enter the Event Description:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Event Pending Verification!")

    st.write(" ")

    st.header("Upcoming Events")

    container = st.container()
    c1, c2, c3, c4 = container.columns(4)
    c1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/earth org.png"), width=150)
    c2.subheader("Event:")
    c2.write("Environmental Earth Day")
    c3.subheader("Organizer:")
    c3.write("Earth.org")
    c4.subheader("Date:")
    c4.write("9/24/2024")
    container.write("Description:")
    container.caption("For Earth Day 2024, EARTHDAY.ORG is unwavering in our commitment to end plastics for the sake of human and planetary health, demanding a 60% reduction in the production of ALL plastics by 2040. Our theme, Planet vs. Plastics, calls to advocate for widespread awareness on the health risk of plastics, rapidly phase out all single use plastics, urgently push for a strong UN Treaty on Plastic Pollution, and demand an end to fast fashion. Join us as we build a plastic-free planet for generations to come!")
    c5, c6 = container.columns(2)
    check = c5.button(label="RSVP", key='4')
    if check:
        c6.write("You're attending the Environmental Earth Day on 9/24/2024!")

    st.write(" ")

    st.header(" ")
    c7, c8, c9, c10 = container.columns(4)
    c7.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/NIU.png"), width=150)
    c8.subheader("Event:")
    c8.write("Chicagoland Safety Health & Environmental Conference")
    c9.subheader("Organizer:")
    c9.write("Northern Illinois University - Naperville Campus")
    c10.subheader("Date:")
    c10.write("9/18/2023")
    container.write("Description:")
    container.caption("The Chicagoland Safety Health & Environmental Conference is a highly anticipated event that brings together industry experts, professionals, and organizations to share knowledge and best practices in creating safe and healthy work environments. Attendees can expect engaging discussions, interactive workshops, and valuable networking opportunities aimed at promoting safety, health, and environmental excellence in various industries.")
    c11, c12 = container.columns(2)
    check = c11.button(label="RSVP", key='5')
    if check:
        c12.write(
            "You're attending the Chicagoland Safety Health & Environmental Conference on 9/18/2023!")

    st.write(" ")

    st.header(" ")
    c13, c14, c15, c16 = container.columns(4)
    c13.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/NCNA.jpeg"), width=150)
    c14.subheader("Event:")
    c14.write("Sustainability Market")
    c15.subheader("Organizer:")
    c15.write("NCNA's Reduce Waste Chicago")
    c16.subheader("Date:")
    c16.write("10/1/2023")
    container.write("Description:")
    container.caption("The Sustainability Market is a gathering place where visitors can meet vendors, artists, organizations and advocates focused on preserving the environment. This year, the market is a single event and will feature representation from a wide range of organizations addressing all aspects of climate change and focusing on helping you live more sustainably. As always, RWC will be hosting their Reuse & Recycling Popup collection tent. ")
    c17, c18 = container.columns(2)
    check = c17.button(label="RSVP", key='6')
    if check:
        c18.write("You're attending Sustainability Market on 10/1/2023!")

    c1, c2, c3, c4 = container.columns(4)
    c1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/WSD.png"), width=150)
    c2.subheader("Event:")
    c2.write("World Spay Day")
    c3.subheader("Organizer:")
    c3.write("The Humane Society Veterinary Medical Association")
    c4.subheader("Date:")
    c4.write("2/28/2024")
    container.write("Description:")
    container.caption("World Spay Day is an annual campaign that aims to encourage people to save animal lives by spaying and neutering companion animals and feral cats. World Spay Day itself is celebrated annually on the fourth Tuesday in February (February 28 in 2023), but your event, no matter how big or small, can take place anytime throughout the month of February, which is recognized as Spay/Neuter Awareness Month.")
    c5, c6 = container.columns(2)
    check = c5.button(label="RSVP", key='7')
    if check:
        c6.write(
            "You're attending the Humane Society Veterinary Medical Association on 2/28/2024!")

    c1, c2, c3, c4 = container.columns(4)
    c1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/WSSD.jpeg"), width=150)
    c2.subheader("Event:")
    c2.write("World Soil Day")
    c3.subheader("Organizer:")
    c3.write("United Nations")
    c4.subheader("Date:")
    c4.write("12/5/2023")
    container.write("Description:")
    container.caption("World Soil Day 2022 (#WorldSoilDay) and its campaign" + "Soils: Where food begins" +
                      "aims to raise awareness of the importance of maintaining healthy ecosystems and human well-being by addressing the growing challenges in soil management, increasing soil awareness and encouraging societies to improve soil health.")
    c5, c6 = container.columns(2)
    check = c5.button(label="RSVP", key='9')
    if check:
        c6.write("You're attending World Soil Day on 12/5/2023!")

    c1, c2, c3, c4 = container.columns(4)
    c1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/WAD.jpeg"), width=150)
    c2.subheader("Event:")
    c2.write("World Animal Day")
    c3.subheader("Organizer:")
    c3.write("UWorld Animal Day")
    c4.subheader("Date:")
    c4.write("10/4/2023")
    container.write("Description:")
    container.caption("It’s a day for all animal lovers near and far. Through organised events, big and small, we raise awareness of how animals are treated globally. We rally together organisations, children’s groups, schools, clubs, companies, communities and individuals to show we care deeply about animals. So whether you’re a grandparent, parent, teenager or toddler, a bird watcher, dog-lover or equestrian, World Animal Day is for all animals and those who love them. With your help, participation in World Animal Day will continue to grow until it connects animal advocates in all corners of the world.")
    c5, c6 = container.columns(2)
    check = c5.button(label="RSVP", key='10')
    if check:
        c6.write("You're attending World Animal Day on 10/4/2023!")


# Map/Home
if selected2 == "Home":

    st.header("Welcome to Nature Nest!")

    st.write("This website is a place for environmental activists and all citziens who are concerned about the environment.")
    st.write("This website serves many purposes:")
    st.write(
        "- Look below for a map of the distribution of CO2 emissions around the globe")
    st.write("- Another tab below shows the environmental nonprofits in the area")
    st.write(
        "- Check out our Events page to host or participate in an environmental event")
    st.write(
        "- Our Purdue page shows environmental information and ways to get involved")
    st.write(
        "- To read and chat about current environmental topics visit the Discuss page")
    st.write("- Go to the Profile page to create and log into your account")

    co2tab, nontab = st.tabs(["CO2 Emissions by Country", "Local Nonprofits"])

    with co2tab:

        df = pd.read_csv('owid-co2-data.csv',
                         usecols=['country', 'co2', "year"])
        df = df[df['year'] == 2021]
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        edata = world.set_index('name').join(df.set_index('country'))

        geojson_data = edata.to_json()

        m = folium.Map(location=[20, 0], zoom_start=2)
        bins = [0, 10, 100, 1000, 10000, 40000]

        st.subheader("CO2 Emissions by Country")

        Choropleth(
            geo_data=geojson_data,
            name="CO2 Emissions",
            data=df,
            columns=['country', 'co2'],
            bins=bins,
            key_on="feature.id",
            fill_color="YlOrRd",
            fill_opacity=1,
            line_opacity=1,
            legend_name="CO2 Emissions by Country"
        ).add_to(m)
        folium_static(m)

    with nontab:

        st.subheader("Local Nonprofits")

        n = folium.Map(location=[40.4237, -86.9212], zoom_start=14)

        tooltip = "Click me!"

        folium.Marker(
            location=[39.8900984463827, -86.14638919999999],
            icon=folium.Icon(color="green", icon='leaf'),
            popup='<a href="https://www.nature.org/en-us/about-us/where-we-work/united-states/indiana/" target="_blank">The Nature Conservancy</a>',
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[39.90370809150084, -86.01175721535616],
            icon=folium.Icon(color="brown", icon='tint'),
            popup='<a href="https://www.mudcreekconservancy.org/" target="_blank">Mud Creek Conservancy</a>',
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[39.77614693875297, -86.15175803177985],
            popup='<a href="https://indianaforestalliance.org/" target="_blank">Indiana Forest Alliance</a>',
            icon=folium.Icon(color="green", icon='tree-conifer'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[39.42788979433591, -86.4286189265558],
            popup='<a href="https://www.hoosierhikerscouncil.org/" target="_blank">Hoosiers Hikers Council</a>',
            icon=folium.Icon(
                color="brown", icon='fa-person-hiking', prefix='fa'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[41.53671228199249, -87.08758460741404],
            popup='<a href="https://heinzetrust.org/" target="_blank">Shirley Heinze Land Trust</a>',
            icon=folium.Icon(color="brown", icon='globe'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[40.419422011239405, -86.87227935286789],
            popup='<a href="https://www.treelafayette.org/" target="_blank">Tree Lafayette</a>',
            icon=folium.Icon(color="green", icon='tree-conifer'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[40.46679429177022, -86.93251920338378],
            popup='<a href="https://www.ctic.org/" target="_blank">Conservation Technology Information Center (CTIC)</a>',
            icon=folium.Icon(color="black", icon='cloud-upload'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[40.423319797340454, -86.89558772924437],
            popup='<a href="https://wabashriver.net/" target="_blank">Wabash River Enhancement Corporation</a>',
            icon=folium.Icon(color="lightblue", icon='tint'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[40.44880073829144, -86.82912640516768],
            popup='<a href="https://nicheslandtrust.org/">NICHES Land Trust</a>',
            icon=folium.Icon(color="brown", icon='globe'),
            tooltip=tooltip
        ).add_to(n)

        folium.Marker(
            location=[40.10999017085569, -85.71083857641723],
            popup='<a href="https://www.whiteriverwatchers.org/">White River Watchers</a>',
            icon=folium.Icon(color="lightblue", icon='tint'),
            tooltip=tooltip
        ).add_to(n)

        folium_static(n)


# Purdue Page
if selected2 == "Purdue":
    st.text(" - An estimated 845,320 metric tons of carbon dioxide was emitted from West Lafayette. ")
    st.text(" - Indiana expects to reduce carbon emissions from our Indiana fleet by 63% by 2030 and 88% by 2040.")
    st.text(" - We hope you can find ways to contribute to reaching this goal!")
    image = Image.open("West Lafayette Emissions.png")
    st.image(image, width=500)
    st.write("Here is the ditribution of West Lafayette Emissions")

    st.divider()

    st.header("Get Involved at Purdue and West Lafayette!")

    rsvp_alt = True
    st.header(" ")
    container = st.container()
    col1, col2, col3, col4 = container.columns(4)
    col1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/p agriculture.png"), width=150)
    col2.subheader("Event:")
    col2.write("Community Nature Day")
    col3.subheader("Organizer:")
    col3.write("Purdue University - College of Agriculture")
    col4.subheader("Date:")
    col4.write("9/22/23")
    container.write("Description:")
    container.caption("This event will be held at the John S. Wright Forestry Center which is located at 1007 North 725 West in West Lafayette. It is on the site of Martell Forest, approximately 7.5 miles west of the West Lafayette campus. Built-in 2002-2003 at a cost of $4 million, the 17,000 sq. ft. Center is a state-of-the-art facility with teaching and research laboratories, office space for faculty and staff, two greenhouses, and a conference center.")
    col4, col5 = container.columns(2)
    check = col4.button(label="RSVP", key="1")
    if check:
        col5.write("You're attending the Community Nature Day on 9/22/23!")

    st.header(" ")

    rsvp_alt = True
    container = st.container()
    col1, col2, col3, col4 = container.columns(4)
    col1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/go greener.jpeg"), width=150)
    col2.subheader("Event:")
    col2.write("Go Greener Commission")
    col3.subheader("Organizer:")
    col3.write("West Lafayette Government")
    col4.subheader("Date:")
    col4.write("10/4/23")
    container.write("Description:")
    container.caption("The Go Greener Commission was established in 2008 in an effort to boost green efforts in the City. The Commission meets in-person the third Tuesday of each month at 6:00pm August - May at West Lafayette City Hall, City Council Chamber. Meets in June and July are virtual. Please contact Lindsey Payne for virtual meeting details. All meets are open to the public.")
    col4, col5 = container.columns(2)
    check = col4.button(label="RSVP", key="2")
    if check:
        col5.write("You're attending the Go Greener Comission on 10/4/23!")

    st.header(" ")

    container = st.container()
    col1, col2, col3, col4 = container.columns(4)
    col1.image(Image.open(
        "/Users/monish/Desktop/Immunization Proof/green trees.jpeg"), width=150)
    col2.subheader("Event:")
    col2.write("West Lafyette Tree Planting Workshop")
    col3.subheader("Organizer:")
    col3.write("Green Trees Organization")
    col4.subheader("Date:")
    col4.write("10/29/23")
    container.write("Description:")
    container.caption("The Green Trees organization is to combat deforestation and environmental degradation by planting a substantial number of trees. We aim to increase global tree coverage and promote reforestation efforts to mitigate climate change and restore ecosystems. Ultimately, Green Trees strives to create a sustainable and greener future for our planet by preserving and enhancing the natural environment through tree planting initiatives.")
    col4, col5 = container.columns(2)
    check = col4.button(label="RSVP", key="3")
    if check:
        col5.write(
            "You're attending the West Lafayette Tree Planting Workshop on 10/29/23!")


# profile page
if selected2 == "Profile":

    if 'user_credentials' not in st.session_state:
        st.session_state.user_credentials = {}

    selected_button = st.sidebar.radio(
        "Choose an option:", ("Login", "Sign-up"))

    if selected_button == "Sign-up":
        st.subheader("Sign-up")
        new_username = st.text_input("Username:")
        new_password = st.text_input("Password:", type="password")

        if st.button("Create Account", key="987"):
            if new_username and new_password:
                if new_username not in st.session_state.user_credentials:
                    st.session_state.user_credentials[new_username] = new_password
                    st.success("Account created successfully!")
                else:
                    st.error(
                        "Username already exists. Please choose another username")
            else:
                st.warning("Please enter a username and password")

    elif selected_button == "Login":
        st.subheader("Login")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")

        if st.button("Login", key="456"):

            if username in st.session_state.user_credentials and st.session_state.user_credentials[username] == password:
                st.success("Login successful!")
            else:
                st.error("Login failed. Please check your username and password.")

if selected2 == "Discuss":

    model_name = "microsoft/DialoGPT-medium"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    st.title("NLP Chatbot")
    user_input = st.text_input("You:", "")

    #FAQ
    if "carbon footprint" in user_input:
        st.write("Your carbon foortprint represents how much carbon you generate per year. Buying an eletric car, carpooling, and reducing waste are all good solutions!")
    elif "recycl" in user_input:
        st.write("Recycling is the process of separating resusable materials. Make sure to recycle to save the environment!")
    elif "environment" in user_input:
        st.write("It's important to preserve the environment. Make sure to recycle and reduce your carbon footprint.")
    else:
        try:
            for step in range(10):
                if st.button("Send", key=87):
                    # take user input
                    text = user_input
                    # encode the input and add end of string token
                    input_ids = tokenizer.encode(
                        text + tokenizer.eos_token, return_tensors="pt")
                    # concatenate new user input with chat history (if there is)
                    bot_input_ids = torch.cat(
                        [chat_history_ids, input_ids], dim=-1) if step > 0 else input_ids
                    # generate a bot response
                    chat_history_ids = model.generate(
                        bot_input_ids,
                        max_length=1000,
                        pad_token_id=tokenizer.eos_token_id,
                    )
                    # print the output
                    output = tokenizer.decode(
                        chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
                    st.write(f"DialoGPT: {output}")
        except Exception as e:
            st.write("")

    st.title("Discussion Section")
    st.header("How can we reduce the use of single-use plastics and plastic waste?")
    # Create a text area for users to enter comments
    user_comment = st.text_area("Write your comment:", max_chars=500, key='0')

    # Create a button to submit comments
    if st.button("Submit Comment", key='3'):
        # Perform some action with the comment (e.g., store it, display it, etc.)
        st.write(user_comment)

# Display existing comments
        st.write("Samuel: I agree with what you are saying. Using reusable alternatives is a practical and impactful way to cut down on single-use plastics. Swapping out items like plastic bags, bottles, and utensils for durable, eco-friendly alternatives made from materials such as cloth, glass, stainless steel, or bamboo significantly reduces our reliance on disposable plastics. ")
    st.header("How can we accelerate efforts to combat climate change?")
    user_comment = st.text_area("Write your comment:", max_chars=500, key='1')
    if st.button("Submit Comment", key='4'):
        # Perform some action with the comment (e.g., store it, display it, etc.)
        st.write(user_comment)
        st.write("Julia: I also think we can encourage international collaboration and agreements, such as the Paris Agreement. Nations must work together to set ambitious goals and commit to reducing greenhouse gas emissions.")
        st.write("Jack: I agree Julia. Another good approach is to invest in research and development of clean technologies, carbon capture and storage, and sustainable agriculture practices. Innovation can lead to breakthrough solutions.")

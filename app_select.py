import streamlit as st

# select / multi select

my_lang = ["Python", "Julia", "Go", "Rust"]
choice = st.selectbox("Language", my_lang)
st.write("You selected {}".format(choice))

# Multiple selection
spoken_lang = ("English", "French", "Spanish", "Chinese", "Indonesia")
my_spoken_lang = st.multiselect("Spoken Lang", spoken_lang, default="English");

# Slider
age = st.slider("Age", 1, 100, 5)

# Selct slider
color = st.select_slider("Choose Color", options=["yellow", "red", "black", "blue", "white"], value=("yellow","red"))
import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname", max_chars=30)
st.title(fname)

# password
st.text_input("Enter password", type='password')

# Text Area
message = st.text_area("Enter Message",height=200)
st.write(message)

# Number
number = st.number_input("Enter Number", 1.0, 25.0, 5.0)

# date input
dateStart = st.date_input("Start From")

# Time input
timeStart = st.time_input("Time start") 

# color picker
color = st.color_picker("select color")
st.write(color)



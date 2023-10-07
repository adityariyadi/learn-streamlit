import streamlit as st

# working with widgets

# Buttons

name = "Scott"

if st.button("submit"):
    st.write("name: {}".format(name.upper()))

if st.button("submit", key='key01'):
    st.write("name: {}".format(name.lower()))    

# Radio
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
elif status == "Inactive":
    st.warning("You are not active")

# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# Beta Expander
if st.expander("Python"):
    st.success("Hello python")

with st.expander("Python"):
    st.text("Hello world")
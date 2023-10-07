import streamlit as st
from PIL import Image

img = Image.open("data/starbucks.png")

# Method config using dictionary

#st.set_page_config(page_title='hello',
#                   page_icon=':smiley:')

PAGE_CONFIG = {"page_title":"Hello", "page_icon":":smiley", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)


# st.set_page_config(page_title='hello',
#                    page_icon=img, layout='wide', initial_sidebar_state='collapsed')

def main():
    st.title("Hello fromstreamlit")
    st.sidebar.success("Menu")



if __name__ == '__main__':
    main()
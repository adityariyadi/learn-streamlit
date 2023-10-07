import streamlit as st

# Image

from PIL import Image

img = Image.open("data\image_03.jpg")
st.image(img,use_column_width=True)

st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg")

# video
video_file = open("data\video.mov","rb").read()
st.video(video_file,start_time=3)

# audio
audio_file = open("data\song.mp3", "rb")
st.audio(audio_file.read())
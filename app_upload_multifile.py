import streamlit as st
from PIL import Image
import os

@st.cache_data
def load_image(imagefile):
    img = Image.open(imagefile)
    return img

def save_uploaded_file(uploadedfile):
    with open(os.path.join("tmpDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    
    return st.success("Saved {} : to tmpDir".format(uploadedfile.name))

def main():
    st.title("Multiple File Uploads")
    menu=["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Upload Multiple Files")
        uploadedfiles = st.file_uploader("Upload Multiple Images", type=['png','jpeg','jpg'], accept_multiple_files=True)
        if uploadedfiles is not None:
            st.write(uploadedfiles)
            for imageFile in uploadedfiles:
                st.write(imageFile.name)
                st.image(load_image(imageFile), width=250)
                save_uploaded_file(imageFile)


if __name__ == '__main__':
    main()



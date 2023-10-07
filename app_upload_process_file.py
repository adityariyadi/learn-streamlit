import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
# import pdfplumber  #not work
from PyPDF2 import PdfReader
import os

# Load images
@st.cache_resource
def load_iamge(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    
    return all_page_text

def save_uploaded_file(uploadedFile):
    with open(os.path.join("tmpDir", uploadedFile.name), "wb") as f:
                f.write(uploadedFile.getbuffer())
    return st.success("saved file : {} in tmpDir".format(uploadedFile.name))


def main():
    st.title("File upload")

    menu = ["Home", "Dataset", "Document Files", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        if image_file is not None:
            # details
            # st.write(type(image_file))
            # methods/attributes
            # st.write(dir(image_file))
            file_details = {"filename": image_file.name, 
                            "filetype": image_file.type,
                            "filesize": image_file.size
                            }
            st.write(file_details)
            st.image(load_iamge(image_file), width=250)

            save_uploaded_file(image_file)

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            # st.write(type(data_file))
            df = pd.read_csv(data_file)
            st.dataframe(df)

            save_uploaded_file(data_file)


    elif choice == "Document Files":
        st.subheader("Document Files")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"filename": docx_file.name, 
                            "filetype": docx_file.type,
                            "filesize": docx_file.size
                            }
                st.write(file_details)

                save_uploaded_file(docx_file)

                if docx_file.type == "text/plain":
                    # read as bytes
                    # raw_text = docx_file.read()
                    raw_text = str(docx_file.read(), "utf-8")
                    st.write(raw_text)
                    st.text(raw_text)
                elif docx_file.type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         pages = pdf.pages[0]
                    #         st.write(pages.extract_text())
                    # except:
                    #     st.write("None")

                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
                    st.text(raw_text)


    else:
        st.subheader("About")


if __name__ == '__main__':
    main()
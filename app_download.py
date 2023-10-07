import streamlit as st;
import streamlit.components as stc
import base64
import time
import pandas as pd


timestr = time.strftime("%Y%m%d-%H%M%S")

def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "new_text_file_{}_.txt".format(timestr)
    st.markdown("#### Donwload File ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

def csv_downloader(data):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "new_text_file_{}_.csv".format(timestr)
    st.markdown("#### Donwload File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Class
class FileDownLoader(object):
    def __init__(self, data, filename='download_file', file_ext='txt'):
        super(FileDownLoader, self).__init__()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = "{}_{}_.{}".format(self.filename, timestr, self.file_ext)
        st.markdown("#### Donwload File ###")
        href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!</a>'
        st.markdown(href, unsafe_allow_html=True)


def main():
    menu = ["Home", "CSV", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":
        st.subheader("Home")
        message = st.text_area("Message")
        if st.button("Save"):
            st.write(message)
            # text_downloader(message)
            download = FileDownLoader(message).download()

    elif choice=="CSV":
        df = pd.read_csv("iris.csv")
        st.dataframe(df)
        # csv_downloader(df)
        download = FileDownLoader(df.to_csv(), file_ext='csv').download()
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()


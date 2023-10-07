import streamlit as st
import pandas as pd
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit Data Editor")

    menu=["Home","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":
        st.subheader("Home")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            df = load_data(data_file)
            with st.form("editor_form"):
                edited_df = st.data_editor(df)
                save_button = st.form_submit_button("Save Data")
                # st.write(dir(data_file))
            
            if save_button:
                # pass
                new_file_name = f"{data_file.name}_{timestr}.csv"
                final_df = edited_df.to_csv()
                st.download_button(label="Download data as CSV", data=final_df, file_name=new_file_name, mime='text/csv')

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
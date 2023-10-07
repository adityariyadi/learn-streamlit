import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app
import logging

# Create A logger
# LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msec)03d -%(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)
# logger = logging.getLogger(__name__)

# Save to file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s %(asctime)s.%(msec)03d -%(message)s")

# File
file_handler = logging.FileHandler('activity.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def main():
    st.title("Main App")
    menu = ["Menu", "EDA", "ML", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Home":
        st.subheader("Home")
        logger.info("Home")
    elif choice=="EDA":
        run_eda_app()
        logger.info("EDA")
    elif choice=="ML":
        run_ml_app()
        logger.info("ML")
    else:
        st.subheader("About")
        logger.info("About")



if __name__ == '__main__':
    main()
import streamlit as st
import pandas as pd

def main():
    
    st.title("Hello")
    st.header("Streamlit Course")
    st.subheader("Introduction")
    st.text("this is test")
    name = "ARS"
    st.text("Testing injecting variable {}".format(name))
    st.markdown("# This is markdown")
    st.success("Success")
    st.warning("Warning")
    st.info("Info")
    st.error("Error")
    st.exception("Exception")


    # Superfunction

    st.write("Normal text")
    st.write("# This is text")
    st.write(1+2)
    st.help(range)
    st.write(dir(st))

    # Display Data
    # Method 1
    df = pd.read_csv("iris.csv")
    st.dataframe(df,600,400)

    # Adding color
    st.dataframe(df.style.highlight_max(axis=0))


    # Method 2
    st.table(df)

    # Method 3
    st.write(df.head())

    # Display json
    st.json({'data':'Scott'})

    # Display Code
    mycode = """
    
        def sayhello():
            print("Hello")

    """
    st.code(mycode, language='python')


if __name__ == '__main__':
    main()
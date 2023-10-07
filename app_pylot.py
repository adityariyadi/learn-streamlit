import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns


def main():
    st.title("Plotting with St.Pyplot")
    df = pd.read_csv("iris.csv")
    st.dataframe(df.head())

    # prev method

    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot()

    # plt.scatter(*np.random.random(size=(2,100)))
    # st.pyplot()

    # Recommended method
    fig,ax=plt.subplots()
    ax.scatter(*np.random.random(size=(2,100)))
    st.pyplot(fig)

    # method 2: simple
    fig = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # method 3
    fig,ax = plt.subplots()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    # Alternatif for matplotlib
    fig = plt.figure()
    sns.countplot(df['species'])
    st.pyplot(fig)

if __name__ == '__main__':
    main()

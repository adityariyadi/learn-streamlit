import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px


def main():
    st.title("Plotting in Streamlit")
    df = pd.read_csv("iris.csv")
    df2 = pd.read_csv("data/lang_data.csv")
    st.dataframe(df.head())

    # Barchart
    st.bar_chart(df[['sepal_length', 'petal_length']])
    

    #Linechart
    st.dataframe(df2.head())
    lang_list = df2.columns.to_list()
    lang_choices = st.multiselect("Choose language", lang_list)
    new_df = df2[lang_choices]
    st.line_chart(new_df)

    #Area chart
    st.area_chart(new_df, use_container_width=True)

    #Altair
    df3 = pd.DataFrame(np.random.randn(200,3), columns=['a','b','c'])
    c = alt.Chart(df3).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.dataframe(df3.head())

    # Method 1
    st.write(c)

    # Method 2 Altair
    st.altair_chart(c, use_container_width=True)

    df3 = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df3)
    fig3 = px.pie(df3, values='Sum', names='lang', title='Pie chart')
    st.plotly_chart(fig3)

    fig4 = px.bar(df3, x='lang', y='Sum')
    st.plotly_chart(fig4)


if __name__ == '__main__':
    main()
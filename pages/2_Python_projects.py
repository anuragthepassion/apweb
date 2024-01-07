import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/images1/photo.jpeg" , width=300)

with col2:
    st.title("Python Application via Self learning")
    content = "    hello , welcome to my website, Below are various project, i worked on as part of learning and gaining first hand experience in developing python applications.   "
    st.info(content)




col3,empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data2.csv", sep=";")

with col3:
    for index, row in df[10:].iterrows():
        #if index % 2 == 0:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/images1/" + row["image"])
        #st.write(row["url"])
        st.write(f"[source code]({row['url']})")


with col4:
    for index, row in df[:10].iterrows():
        #if index % 2 != 0:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/images1/" + row["image"])
        #st.write(row["url"])
        st.write(f"[source code]({row['url']})")
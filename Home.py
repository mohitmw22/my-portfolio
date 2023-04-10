import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

content="""
This code is supposed to show how good the company is. The kind of people 
that work here, the kind of culture that can be experienced here and the 
kind of product that is developed here show exactly why this is the best 
company."""
st.write(content)

st.header("Our Team")

col1, col2, col3 =st.columns(3)

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
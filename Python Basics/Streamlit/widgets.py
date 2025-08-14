import streamlit as st
import pandas as pd

st.title('Streamlit text input')

name=st.text_input("enter your name :")

age=st.slider("select your age",0,100,25)
st.write(f"Your age is {age}")

options = ['Python','Java','JS','TS']
choices = st.selectbox("Choose your favoraite language :",options)
if name:
    st.write(f"Hello, {name}")
st.write(f"Your language is {choices} .")

data={
    "Name":['Sam','Bailey','Dean','Krish'],
    "Age":[22,32,32,43],
    "City":['San Fransisco',"LA",'Auckland',"Sao Paulo"]
}

df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
# if name:
#     st.write(f"Hello, {name}")
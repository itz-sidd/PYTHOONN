import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit")

#Displaying text
st.write("text pages")

df=pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[332,423,52525,25,2]
})

st.write("Here is the dataframe")
st.write(df)

#Line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
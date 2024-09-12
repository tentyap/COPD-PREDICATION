# Loading and display  data
import streamlit as st
import pandas as pd


# title 
st.title("Data Display in streamlit")

# Load the data 
path=r"C:\Users\kamal\OneDrive\Desktop\steamline\sample_dataset (2).csv"
df = pd.read_csv(path)

# display  the data set
st.write("dataset")
st.dataframe(df)

# Display the summery of my dataset

st.write("summary")

st.write(df.describe())

# visulize of our data


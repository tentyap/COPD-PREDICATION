# visulize a data in streamlit
# import all the necessary libary need
import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# title
st.title("Data Visualization with streamlit")

#Load a data
path=r"C:\Users\kamal\OneDrive\Desktop\steamline\sample_dataset (2).csv"

df = pd.read_csv(path)

# create a histogram using a sesaborn
fig, ax = plt.subplots()
sns.histplot(df['age'], bins = 10, kde =True, ax=ax)
st.pyplot(fig)



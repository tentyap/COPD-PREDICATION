import streamlit as st

st.title("Intrective widgets")
# st.write("This is a simple to demonestrate streamlite feature ")


# Text input
name = st.text_input("Enter your Name: ")

age = st.slider("select your age:",18 ,80,1)

# Button
if st.button("Submit"):
    st.write(f'Hello,{name}!,you are {age} years old. ')

# Load data 
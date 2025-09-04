#Run this program by using this command: 
#python -m streamlit run Main/webapp_streamlitapp.py

import streamlit as st

st.title("My simple streamlit web app!")
st.header("This is a sample header!")
st.write("This is a sample para.")

name=st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}!")

age=st.slider("Select your age",1,100,25)
st.write("Your selected age is: ",age)
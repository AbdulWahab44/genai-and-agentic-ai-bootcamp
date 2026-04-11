# Basics 
import streamlit as st

st.title("Welcome to My Website")
st.write("compay Intro ...")


# This is all about buttons widget in streamlit.
if st.button("button 1", type="primary"):
    st.write("Lets celebrate your clicking 1")
    st.balloons()


if st.button("button 2", type="secondary"):
    st.write("Lets celebrate your clicking 2")
    
st.button("button 3", type="tertiary")
st.button("button 4")
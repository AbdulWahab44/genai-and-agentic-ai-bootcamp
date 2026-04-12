# Project: BMI Calculator
import streamlit as st

st.header("Project : BMI Calculator")

weight_kg = st.slider("Enter your weight in (kg)", 30, 300, 70, key="bmi_weight")
st.write(weight_kg)

height_cm = st.slider("Enter your height in (cm)", 100, 250, 170, key="bmi_height")
st.write(height_cm)

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"
    
    
st.metric(f"Your BMI", f"{bmi:.2f}")
st.info(f"Your BMI category is: {category}")
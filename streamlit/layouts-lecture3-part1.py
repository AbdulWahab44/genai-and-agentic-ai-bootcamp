import streamlit as st

st.title("Streamlit Layouts Demo")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first left column.")
    
    with st.form("user_form"):
        f_name = st.text_input("First Name")
        l_name = st.text_input("Last Name")
        email = st.text_input("Email")
        f_age = st.number_input("Age", min_value=0, max_value=120, value=18)    
        submit_button = st.form_submit_button("Submit")
    
        if submit_button:
            st.success(f"Form Submitted! Name: {f_name} {l_name}, Email: {email}, Age: {f_age}, Thank you!" )

with col2:
    st.header("Column 2")
    st.write("This is the second right column.")   
    
    date = st.date_input("Select a date:")
    st.write(f"You selected the date: {date}")

    time = st.time_input("Select a time:")
    st.write(f"You selected the time: {time}")

    color = st.color_picker("Pick a color:", "#00ff00")
    st.write(f"You picked the color: {color}")

    uploaded_file = st.file_uploader("Upload a file:")
    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!") 
        
    

with st.expander(" See More Details 1"):
    st.write("You can hide some content here that can be seen when the user clicks to expand.")
    
with st.expander(" See More Details 2"):
    st.write("You can hide some content here that can be seen when the user clicks to expand.")
    
with st.expander(" See More Details 1"):
    st.write("You can hide some content here that can be seen when the user clicks to expand.")
    

#
st.sidebar.title("left sidebar")
options = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {options}")

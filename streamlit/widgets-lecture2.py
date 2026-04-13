import streamlit as st

st.title("Streamlit Widgets Demo")
st.write("""
         This is an application to show different widgets in Streamlit.\n
         This is an application to show different widgets in Streamlit.\n
         This is an application to show different widgets in Streamlit.
         """)

# 1. Text Input Widgets
st.header("1. Text Input Widgets")

name = st.text_input("Enter your name:", placeholder="Type your name here...")
bio = st.text_area("Tell us about yourself:", placeholder="Write something about you...")
password = st.text_input("Password: ", type="password")

if name:
    st.success(f"Hello, {name}! Welcome to Streamlit.")

if bio:
    st.success(f"Thank you for sharing about yourself!\n{bio}") 
    
# 2. Number and Slider Widgets
st.header("2. Number and Slider Widgets")

age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)

st.write(f"Your age is {age}")

rating = st.slider("Rate your experience with Streamlit:", min_value=0, max_value=10, value=5)
st.write(f"Your rating is {rating}")


# 3. Selection Widgets
st.header("3. Selection Widgets")

subscribe = st.checkbox("Subscribe to our newsletter")

if subscribe:
    st.success("Thank you for subscribing!")
else:
    st.warning("You have not subscribed to our newsletter.")
    
language = st.radio("Select your favorite programming language:", ("Python", "JavaScript", "Java", "C++"))
st.write(f"Your favorite programming language is {language}")

hobies = st.multiselect(
    "Select your hobbies:",
    ["Reading", "Traveling", "Cooking", "Sports"]
    )
st.write(f"Your hobbies are: {', '.join(hobies)}" if hobies else "You have not selected any hobbies.")
# 
# # OR
# if hobies:
#     ans = ", ".join(hobies)
#     st.write(f"Your hobbies are: {ans}")
# else:
#     st.write("You have not selected any hobbies.")


# 4. Buttons and Event handling
st.header("4. Buttons and Event handling")

if st.button("Click Me!"):
    st.balloons()
    st.success("You clicked the button!")
    
if st.button("Show Alert"):
    st.toast("This is a Streamlit toast message!")
    st.write("You clicked the alert button!")
    
if st.button("Show Error"):
    st.error("An error occurred!")
    st.write("You clicked the error button!")
    
    
# 5. Special Widgets like Date, Time, File Uploader, Color Picker
st.header("5. Special Widgets")

date = st.date_input("Select a date:")
st.write(f"You selected the date: {date}")

time = st.time_input("Select a time:")
st.write(f"You selected the time: {time}")

color = st.color_picker("Pick a color:", "#00ff00")
st.write(f"You picked the color: {color}")

uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file:
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    
    
# 6. Form - Grouping Widgets
st.header("6. Using Forms (Grouped Widgets)")

with st.form("user_form"):
    f_name = st.text_input("First Name")
    l_name = st.text_input("Last Name")
    email = st.text_input("Email")
    f_age = st.number_input("Age", min_value=0, max_value=120, value=18)    
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        st.success(f"Form Submitted! Name: {f_name} {l_name}, Email: {email}, Age: {f_age}, Thank you!" )  
        
        
# 7. Seasion State (state of widgets)
st.header("7. Session State (State of Widgets)")

if "counter" not in st.session_state:
    st.session_state.counter = 0
    
if st.button("Increment Counter"):
    st.session_state.counter = st.session_state.counter + 1
    
st.write(f"Counter value: {st.session_state.counter}")
    
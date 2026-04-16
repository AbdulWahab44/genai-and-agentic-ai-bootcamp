import streamlit as st
import pandas as pd

st.title("Streamlit Charts Demo")

# Create a sample dataset
data = {
    "Name": ["Wahab", "Ali", "Zain", "Safi"],
    "Age": [25, 30, 22, 28],
    "City": ["Karachi", "Lahore", "Islamabad", "Peshawar"]
}

df = pd.DataFrame(data)

st.write("Here is the Table:")
st.dataframe(df) # Display the DataFrame as a table

st.write("Here is the Line Chart:")
st.line_chart(df) # Display the DataFrame as a line chart

#
tab1, tab2 = st.tabs(["Dataframe Table", "Line Chart"])
tab1.dataframe(df) # Display the DataFrame in the first tab
tab2.line_chart(df) # Display the line chart in the second tab

#
with st.container(border=True):
    st.write("This is a container with a border.")
    st.write("You can put any content inside this container.")
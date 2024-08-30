import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("Bar Chart Creator")

# Instructions
st.write("Enter the labels and corresponding values to create a bar chart.")

# Input form for labels and values
labels = st.text_input("Enter labels (comma-separated)", "Label1,Label2,Label3")
values = st.text_input("Enter values (comma-separated)", "10,20,30")

# Convert input strings to lists
label_list = labels.split(",")
value_list = list(map(int, values.split(",")))

# Check if the input is valid
if len(label_list) == len(value_list):
    # Create a dataframe from the input data
    data = pd.DataFrame({"Labels": label_list, "Values": value_list})

    # Display the dataframe
    st.write("Input Data:")
    st.write(data)

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(data['Labels'], data['Values'])
    ax.set_xlabel("Labels")
    ax.set_ylabel("Values")
    ax.set_title("Bar Chart")

    # Display the bar chart
    st.pyplot(fig)

else:
    st.error("The number of labels and values must match.")

# Option to download the data as CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(data)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='bar_chart_data.csv',
    mime='text/csv',
)

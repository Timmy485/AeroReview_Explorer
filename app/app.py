import streamlit as st
import plotly.express as px
import pandas as pd
import base64
from collections import Counter
import os
# from . import config

st. set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .appview-container .main .block-container {
        padding-top: 2rem;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


path = os.path.dirname(__file__)
my_file = path+'/media/plane.jpg'
set_bg_hack(my_file)

# Set the title and subtitle with background color
st.markdown(
    "<h1 style='text-align: center; padding: 10px;'>AEROREVIEW EXPLORER</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; padding: 2px;'>Analyze Sentiment Trends of British Airways Flights</h3>",
    unsafe_allow_html=True
)

# Sidebar Navigation with header background color
st.sidebar.markdown(
    "<h3 style= padding: 10px;'>Navigation</h3>",
    unsafe_allow_html=True
)


# Use a dropdown menu for feature selection
selected_feature = st.sidebar.selectbox("Select a Feature", (
    "Sentiment Distribution", "Data Visualization",  "Word Clouds",
    "Topic Modeling", "Real-time Sentiment Analysis", "Sentiment Trends by Aspect",
    "Predictive Insights"))


# Main Content with light background color
st.markdown(
    "<div style='background-color: #f9f9f9; padding: 0px;'>",
    unsafe_allow_html=True
)


if selected_feature == "Sentiment Distribution":
    # Sentiment Distribution Content
    st.header("Sentiment Distribution")

    # Sample sentiment data

    counts = [50, 30, 20]  # Replace with your actual sentiment counts

    current_directory = os.path.dirname(__file__)
    # Construct the path to data.csv
    data_csv_path = os.path.join(
        current_directory, '../data/review_sentiment_df.csv')

    df = pd.read_csv(data_csv_path)
    sentiments = ["Positive", "Negative", "Neutral"]
    count = Counter(df['sentiments'])
    counts = [count['Positive'], count['Negative'], count['Neutral']]

    # Create a pie chart with custom size
    fig = px.pie(
        names=sentiments,
        values=counts,
        title="Sentiment Distribution for Verified Reviews",
        labels={"names": "Sentiment"},
        width=1000,  # Set the width
        height=800,  # Set the height
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
                      plot_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(legend=dict(font=dict(size=20)))
    fig.update_layout(
        title_text="Sentiment Distribution for Verified Reviews", title_font=dict(size=20))

    # Display the chart on your Streamlit app
    st.plotly_chart(fig)

    total_observations = sum(counts)
    st.write(f"Total observations: {total_observations}")

    # Create a table to display counts
    data = {"Sentiment": sentiments, "Count": counts}
    df = pd.DataFrame(data)
    st.table(df)


elif selected_feature == "Data Visualization":
    # Data Visualization Content
    st.header("Data Visualization")
    # Include interactive charts and graphs here.

elif selected_feature == "Word Clouds":
    # Word Clouds Content
    st.header("Word Clouds & Frequency Analysis")
    # Include word clouds for positive, negative, and neutral sentiments.

elif selected_feature == "Geographical Insights":
    st.header("Geographical Insights")

elif selected_feature == "Topic Modeling":
    st.header("Topic Modeling")

elif selected_feature == "Real-time Sentiment Analysis":
    st.header("Real-time Sentiment Analysis")

elif selected_feature == "Comparative Analysis":
    st.header("Comparative Analysis")

elif selected_feature == "Sentiment Trends by Aspect":
    st.header("Sentiment Trends by Aspect")

elif selected_feature == "Predictive Insights":
    st.header("Predictive Insights")
# Close the background div for the main content
st.markdown("</div>", unsafe_allow_html=True)


# Footer with a subdued color
st.markdown(
    "<div style='position: fixed; bottom: 0; left: 0; width: 100%; text-align: right;'>"
    "<p style='color: #999;'>AeroReview Explorer by Yeboah Timothy</p>"
    "</div>",
    unsafe_allow_html=True
)

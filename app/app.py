import streamlit as st
import plotly.express as px
import pandas as pd
from collections import Counter
from helpers import set_bg_hack, calculate_word_frequency, plot_barplot, plot_wordcloud
import os


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


path = os.path.dirname(__file__)
my_file = path+'/media/plane.jpg'
set_bg_hack(my_file)



# Construct the path to data.csv
current_directory = os.path.dirname(__file__)
data_csv_path = os.path.join(
    current_directory, 
    '../data/sentiments_without_stopwords.csv')

df = pd.read_csv(data_csv_path)
positive_reviews = df[df['sentiments'] == 'Positive']
negative_reviews = df[df['sentiments'] == 'Negative']
neutral_reviews = df[df['sentiments'] == 'Neutral']



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

    # Create two equal-length columns
    col1, col2 = st.columns(2)

    # Positve Reviewsws Content
    with col1:
        st.write("Positive Reviews")
        freqdist = calculate_word_frequency(positive_reviews['reviews'])
        top_words = freqdist.most_common(11)
        
        plot_barplot(freqdist, text='Top 10 frequent words in positive reviews')

        df = pd.DataFrame(top_words[1:], columns=['Words', 'Count'])
        st.table(df)

   # Negative Reviewsws Content
    with col2:
        st.write("Negative Reviews")
        freqdist = calculate_word_frequency(negative_reviews['reviews'])
        top_words = freqdist.most_common(11)
        
        plot_barplot(freqdist, text='Top 10 frequent words in negative reviews')

        df = pd.DataFrame(top_words[1:], columns=['Words', 'Count'])
        st.table(df)

elif selected_feature == "Word Clouds":
    # Word Clouds Content
    st.header("Word Clouds & Frequency Analysis")
    # Include word clouds for positive, negative, and neutral sentiments.

    col1, col2 = st.columns(2)
    with col1:
        st.write("Positive Word Cloud")

    with col2:
        st.write("Negative Word Cloud")


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

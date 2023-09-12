import streamlit as st
import json
import google.generativeai as palm
import base64
import plotly.express as px
import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import nltk
nltk.download('punkt')


st. set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .appview-container .main .block-container {
        padding-top: 2rem;
        margin: 0;
    }
    .css-usj992 {
    background-color: transparent;
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

# Construct the path to data.csv
current_directory = os.path.dirname(__file__)
data_csv_path = os.path.join(
    current_directory, 
    '../data/sentiments_without_stopwords.csv')

df = pd.read_csv(data_csv_path)
positive_reviews = df[df['sentiments'] == 'Positive']
negative_reviews = df[df['sentiments'] == 'Negative']
neutral_reviews = df[df['sentiments'] == 'Neutral']



def calculate_word_frequency(df):
    # Tokenize the text data
    tokens = word_tokenize(' '.join(df))
    tokens = [word.strip(",.-") for word in tokens]

    # Perform frequency analysis
    freqdist = FreqDist(tokens)
    return freqdist

def plot_barplot(freqdist, text=''):
    top_words = freqdist.most_common(10)  # Get the top 10 most frequent words
    top_words.pop(0)  # Remove the most common word (usually a stop word)
    
    # Create a DataFrame for the top words
    df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
    
    # Create a bar plot using Plotly Express
    fig = px.bar(df, x='Frequency', y='Word', orientation='h', title=f'Top 10 most frequent words {text}')
    
    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)

def plot_wordcloud(freqdist):  
    wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=100, contour_width=3, contour_color='steelblue')
    wordcloud.generate_from_frequencies(freqdist)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    
    st.pyplot(fig)

def get_sentiment(input, model, temperature=0):
    prompt = "You are an expert at sentiment analysis.\n\n"
    prompt += "Return the sentiment (Positive, Negative, or Neutral) for each review:\n"
    prompt += f"Review: {input}\n"

    response  = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    )
    return response.result


# Read the content of the config.json file
json_path = path+'/config.json'
try:
    with open(json_path, 'r') as config_file:
        config_data = json.load(config_file)
    api_key = config_data.get('key')
except FileNotFoundError:
    # If the config.json file is not found, try reading from Streamlit Secrets
    try:
        api_key = st.secrets["PALM_API"]
    except st.secrets.SecretsFileNotFound:
        st.error("Please provide the API key either in a 'config.json' file or as a Streamlit Secret.")
        st.stop()

palm.configure(api_key=api_key)





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
    st.header("Word Clouds")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Positive Reviews Word Cloud")
        freqdist = calculate_word_frequency(positive_reviews['reviews'])
        top_words = freqdist.most_common(11)
        plot_wordcloud(freqdist)

    with col2:
        st.write("Negative Reviews Word Cloud")
        freqdist = calculate_word_frequency(negative_reviews['reviews'])
        top_words = freqdist.most_common(11)
        plot_wordcloud(freqdist)


elif selected_feature == "Geographical Insights":
    st.header("Geographical Insights")




elif selected_feature == "Topic Modeling":
    st.header("Topic Modeling")




elif selected_feature == "Real-time Sentiment Analysis":
    st.header("Real-time Sentiment Analysis")

    prompt = st.chat_input("Input Review...")
    if prompt:
        st.write(f"Sentiment: {get_sentiment(prompt, 'models/text-bison-001')}")




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

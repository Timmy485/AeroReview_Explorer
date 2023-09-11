import base64
import plotly.express as px
import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud
import nltk
import pandas as pd
nltk.download('punkt')

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

# def plot_wordcloud(freqdist):  
#     wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=100, contour_width=3, contour_color='steelblue')
#     wordcloud.generate_from_frequencies(freqdist)
#     plt.figure(figsize=(8, 8))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     plt.show()




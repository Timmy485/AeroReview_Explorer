import streamlit as st
# from . import config

st. set_page_config(layout ="wide")
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
# Set the title and subtitle with background color
st.markdown(
    "<h1 style='text-align: center; padding: 10px;'>AEROREVIEW EXPLORER</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; padding: 2px;'>Analyze Sentiment Trends of British Airways Flights</h3>",
    unsafe_allow_html=True
)
st.image("app/media/robo.jpg",
             use_column_width=True,
             )

# Sidebar Navigation with header background color
st.sidebar.markdown(
    "<h3 style= padding: 10px;'>Navigation</h3>",
    unsafe_allow_html=True
)


# Use a dropdown menu for feature selection
selected_feature = st.sidebar.selectbox("Select a Feature", (
    "Sentiment Distribution", "Data Visualization",  "Word Clouds", 
    "Topic Modeling", "Real-time Sentiment Analysis", "Geographical Insights", 
    "Comparative Analysis", "Sentiment Trends by Aspect", "Predictive Insights"))



# Main Content with light background color
st.markdown(
    "<div style='background-color: #f9f9f9; padding: 0px;'>",
    unsafe_allow_html=True
)


if selected_feature == "Sentiment Distribution":
    # Sentiment Distribution Content
    st.header("Sentiment Distribution")
    # Include sentiment distribution chart.

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

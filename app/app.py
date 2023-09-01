import streamlit as st


# Set the title and subtitle with background color
st.markdown(
    "<h1 style='text-align: center; background-color: #f0f0f0; padding: 10px;'>AeroReview Explorer</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; background-color: #f0f0f0; padding: 10px;'>Analyze Sentiment Trends of British Airways Flights</h3>",
    unsafe_allow_html=True
)

# Sidebar Navigation with header background color
st.sidebar.markdown(
    "<h3 style='background-color: #c0e6e6; padding: 10px;'>Navigation</h3>",
    unsafe_allow_html=True
)
selected_feature = st.sidebar.radio(
    "Select a Feature",
    ("Data Visualization", "Sentiment Distribution", "Word Clouds", "Geographical Insights",
     "Topic Modeling", "Real-time Sentiment Analysis", "Comparative Analysis", "Sentiment Trends by Aspect", "Predictive Insights")
)

# Main Content with light background color
st.markdown(
    "<div style='background-color: #f9f9f9; padding: 20px;'>",
    unsafe_allow_html=True
)

if selected_feature == "Data Visualization":
    # Data Visualization Content
    st.header("Data Visualization")
    # Include interactive charts and graphs here.

elif selected_feature == "Sentiment Distribution":
    # Sentiment Distribution Content
    st.header("Sentiment Distribution")
    # Include sentiment distribution chart.

elif selected_feature == "Word Clouds":
    # Word Clouds Content
    st.header("Word Clouds")
    # Include word clouds for positive, negative, and neutral sentiments.

# Continue with similar sections for other features

# Close the background div for the main content
st.markdown("</div>", unsafe_allow_html=True)

# Footer with a subdued color
st.markdown(
    "<p style='text-align: center; color: #999;'>AeroReview Explorer by Your Name</p>",
    unsafe_allow_html=True
)

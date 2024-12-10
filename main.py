import requests
import streamlit as st

# Securely load the API key
api_key = st.secrets["newsapi_key"]

st.title('News App by Sasanka 🧐')
st.write('This is a simple news app built with Streamlit and NewsAPI')

# Input field to get the topic & search button aligned to right
input = st.text_input('Enter the topic you want to search for:')
search = st.button('Search')

if search:
    if input:
        url = f'https://newsapi.org/v2/everything?q={input}&sortBy=publishedAt&apiKey={api_key}'  
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP issues
            content = response.json()
            
            # Check if there are articles
            if content.get('articles'):
                for post in content['articles']:
                    st.write(post['title'])
                    st.write(post['description'])
                    st.write(post['url'])
                    st.write(f"⏳: {post['publishedAt']}")
                    st.write('---')
            else:
                st.write("No articles found for this topic.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        # Show a warning only when the search button is clicked with no input
        st.warning("Please enter a topic to search for news.")

# A Streamlit app to search for news articles and send them to the user's email

import requests
import streamlit as st
import smtplib
import ssl

# Securely load the secrets
api_key = st.secrets["newsapi_key"]
username = st.secrets["email"]
password = st.secrets["password"]

# format content to be sent to the email
def format_content(content):
    # Get the top 10 articles in a loop and format them and return them as a string
    formatted_content = ""
    for i in range(10):
        formatted_content += f"{content['articles'][i]['title']}\n{content['articles'][i]['url']}\n-----\n\n"
    return formatted_content

# Send the news to the user's email with smtplib.SMTP_  
def send_news_to_email(email,content):
    host = "smtp.gmail.com"
    port = 465

    if email:
        subject = "Latest news articles"
        body = format_content(content)

        # Encode the message in UTF-8
        message = f"Subject: {subject}\n\n{body}".encode('utf-8')
        try:
            # Create an SSL context
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(username, password)
                server.sendmail(username, email, message)
                st.success("Email sent successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Search for news
def search_news(input):
    url = f'https://newsapi.org/v2/everything?q={input}&sortBy=publishedAt&apiKey={api_key}'  
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        content = response.json()
        return content
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    
# Display the news
def display_news(content):
    if content.get('articles'):
        for post in content['articles']:
            st.write(post['title'])
            st.write(post['description'])
            st.write(post['url'])
            st.write(f"⏳: {post['publishedAt']}")
            st.write('---')

# Tabs for Viewing and Sending news
tab1, tab2 = st.tabs(["Search for News", "Send News to Email"])

with tab1:
    # Title and description
    st.title('News App by Geethika 🧐')
    st.write('This is a simple news app built with Streamlit and NewsAPI')

    # Searching part for news
    # Input field to get the topic & search button aligned to right
    input = st.text_input('Enter the topic you want to search for:', key='input_topic_search')
    search = st.button('Search')

    if search:
        if input:
            content = search_news(input)
            if content:
                # Check if there are articles
                if content.get('articles'):
                    display_news(content)   
                else:
                    st.write("No articles found for this topic.")
        else:
            # Show a warning only when the search button is clicked with no input
            st.warning("Please enter a topic to search for news.")


with tab2:
    # Sending news to the user's email
    # if topic is not defined in the 'Search for News' tab, get the news topic from the user
    if not input:
        input = st.text_input('Enter the topic you want to search for:', key='input_topic_email')

    if input:
        content = search_news(input)

    # Get the user's email and send the news. Input Box for email and a button to send
    # Input Box for email
    email = st.text_input('Enter your email:', key='input_email_email')

    # Button to send
    send = st.button('Send')

    if send:
        if email:
            send_news_to_email(email, content)
        else:
            st.warning("Please enter your email to send the news.")




# BASIC Sasa News App 🔍📰

Sasa News App is a streamlined Streamlit application that allows users to search for news articles on any topic and optionally have them delivered directly to their email inbox. Built with simplicity and functionality in mind, this app leverages the NewsAPI to fetch current articles and presents them in an easy-to-read format.

## Features ✨

- **News Search** 🔎: Search for articles on any topic using the NewsAPI
- **Clean Display** 📋: View article titles, descriptions, URLs, and publication times in a well-formatted layout
- **Email Delivery** 📧: Send the top 10 search results directly to your email
- **User-Friendly Interface** 🖥️: Simple two-tab design separating search and email functionality

## Technical Implementation 🛠️

The app is built using:
- **Streamlit** 🌊: For the web interface and UI components
- **NewsAPI** 📰: To fetch relevant news articles based on user queries
- **SMTP** 📨: For sending emails via Gmail
- **SSL** 🔒: For secure email transmission

The codebase is organized into clear functions:
- `search_news()`: Handles API requests to NewsAPI
- `display_news()`: Formats and displays articles in the Streamlit interface
- `format_content()`: Prepares article data for email delivery
- `send_news_to_email()`: Manages the email sending process

## Security 🔐

The application uses Streamlit's secrets management to securely store:
- NewsAPI key
- Email credentials

This prevents sensitive information from being exposed in the codebase.

## Usage 📱

Users can:
1. Enter a topic in the search tab to view current news articles
2. Switch to the email tab to have articles on their chosen topic sent to their email address
3. Receive a formatted email containing titles and links to the top 10 most recent articles

## Limitations ⚠️

- Currently limited to the free tier of NewsAPI
- Email delivery is configured for Gmail only
- No persistent storage of user preferences or search history

This project serves as a practical example of combining web APIs, email functionality, and a clean user interface in a Streamlit application. 🚀

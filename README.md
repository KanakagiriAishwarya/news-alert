📰 Automated Crawling, Categorization and Sentiment Analysis of Digital News with Feedback System
📌 Project Overview

In today’s digital world, massive amounts of news are published every second. Many of these articles are biased, misleading, or emotionally charged, making it difficult for citizens and government agencies to track reliable and actionable insights.

This project provides an AI-powered end-to-end pipeline that:

Crawls real-time news articles from multiple online sources.

Preprocesses text (cleaning, tokenization, lemmatization).

Translates regional language news into English for uniform processing.

Performs Sentiment Analysis (Positive / Neutral / Negative).

Classifies news into relevant Government Departments (Health, Education, Transport, etc.).

Sends Automated Email Alerts to concerned departments for negative news.

Displays results in a clean, web-based dashboard with filtering options.

🚀 Features

🌐 Web Crawling – Extract news from static & dynamic websites.

🔤 Multilingual Support – Translate regional language news into English.

📊 Sentiment Analysis – Detect tone (positive, negative, neutral).

🏛 Categorization – Classify articles into government departments.

📩 Feedback System – Real-time email alerts for negative news.

💻 User Interface – Filter by department, sentiment, and language.

🛠️ Tech Stack
Languages & Frameworks

Python – Core backend

Flask / Streamlit – Web UI

HTML, CSS, JavaScript – Frontend design

Libraries & Tools

Web Scraping: BeautifulSoup, Selenium, Newspaper3k

NLP & Preprocessing: spaCy, NLTK, Google Translate API

Sentiment Analysis: TextBlob, VADER, DistilBERT (Hugging Face)

Classification: Scikit-learn (Logistic Regression, Naïve Bayes, SVM), TF-IDF, KMeans

Email Alerts: smtplib (Python’s Simple Mail Transfer Protocol Library)

Storage: SQLite / MongoDB

Version Control: Git & GitHub

⚙️ System Workflow

Data Crawling → Collect articles using BeautifulSoup/Selenium/Newspaper3k.

Preprocessing → Clean text (remove stopwords, lemmatize using spaCy/NLTK).

Translation → Use Google Translate API for non-English articles.

Sentiment Analysis → Classify news as Positive, Neutral, or Negative.

Categorization → Map news to relevant government departments.

Feedback System → Send email alerts to departments if sentiment = Negative.

Visualization → Show categorized news in an interactive dashboard.

📊 Results

🏷 Department Classification Accuracy: ~92% (Logistic Regression)

🙂 Sentiment Analysis Accuracy: ~88% (Naïve Bayes)

⏱ Real-time performance: ~200 ms/article

📩 Email alert delivery: < 5 seconds

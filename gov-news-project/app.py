import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---- 1. Load and Preprocess Data ----
@st.cache_data
def load_data():
    df = pd.read_csv("processed_english_news.csv")
    
    # Treat neutral as negative
    df['sentiment'] = df['sentiment'].replace({'neutral': 'negative'})
    
    return df

df = load_data()

# ---- 2. Sidebar Filter ----
st.sidebar.title("Filter News")
sentiment_choice = st.sidebar.selectbox("Sentiment", options=['all', 'positive', 'negative'])

if sentiment_choice != 'all':
    filtered_df = df[df['sentiment'] == sentiment_choice]
else:
    filtered_df = df

# ---- 3. Main Display ----
st.title("📰News Alert System")
st.write("News items are shown based on sentiment")

# ---- 4. Display News Table ----
st.dataframe(filtered_df[['title', 'sentiment']].head(20))

# ---- 5. Email Configuration ----
sender_email = "grishma7645@gmail.com"
receiver_email = "grishmag1404@gmail.com"
password = "uhul lcyp rqkg dogd"
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email_alert(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# ---- 6. Email Button ----
st.subheader("📬 Send Email Alerts for Negative News ")

if st.button("Send Alerts"):
    negative_df = df[df['sentiment'] == 'negative']

    if negative_df.empty:
        st.success("✅ No negative news found to alert.")
    else:
        for index, row in negative_df.iterrows():
            title = row['title']
            content = row['content']
            subject = f"ALERT: Negative News Detected - {title}"
            body = f"Title: {title}\n\nContent: {content}\n\nThis news has been flagged for attention."
            success = send_email_alert(subject, body)
            if success:
                st.info(f"Alert sent for: {title}")

# scripts/email_alert.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "grishma7645@gmail.com"
receiver_email = "grishmag1404@gmail.com"
password = "uhul lcyp rqkg dogd"  # Use a Gmail App Password

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
            print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

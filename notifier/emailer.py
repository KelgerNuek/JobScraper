import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
TO = os.getenv("TO")

def send_email(job_list):
    if not job_list:
        return

    body = "\n\n".join([f"{j['title']} at {j['company']}\n{j['url']}" for j in job_list])
    msg = MIMEText(body)
    msg["Subject"] = "My Daily Job Digest"
    msg["From"] = EMAIL
    msg["To"] = TO

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, TO, msg.as_string())
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

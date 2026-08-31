import os
import smtplib
import ssl
from email.message import EmailMessage

email_sender = os.environ.get("EMAIL_SENDER")
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = os.environ.get("EMAIL_RECEIVER")
subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em[" subject"] = subject
em.set_content(body)


context = ssl.create_default_context()

if not email_sender or not email_password:
    raise ValueError("EMAIL_SENDER/EMAIL_PASSWORD env vars required")
if not email_receiver:
    raise ValueError("EMAIL_RECEIVER env var required")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

from email.message import EmailMessage
import ssl
import smtplib
import environ
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True)
env = environ.Env()
READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE", default=True)  # type: ignore  # noqa: PGH003
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))
email_sender = env(
    "EMAIL_SENDER",
    default="rhixecompany@gmail.com",  # type: ignore  # noqa: PGH003
)
email_password = env(
    "EMAIL_PASSWORD",
    default="",  # type: ignore  # noqa: PGH003
)
email_receiver = env(
    "EMAIL_RECEIVER",
    default="",  # type: ignore  # noqa: PGH003
)

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

from os import getenv
from flask import url_for
from itsdangerous import URLSafeTimedSerializer
from email.message import EmailMessage
import smtplib
import ssl


SERIALIZE = URLSafeTimedSerializer(getenv('SECRET_KEY'))


def send_email_token(email: str) -> str:
    try:
        token = SERIALIZE.dumps(email, salt='email-confirm')

        link = url_for('.confirm_email', token=token, _external=True)

        subject_msg = 'Confirm Email'
        body_msg = f'Your link is {link}'

        em = EmailMessage()
        em['From'] = getenv('MAIL_USER')
        em['To'] = email
        em['Subject'] = subject_msg
        em.set_content(body_msg)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL(getenv('MAIL_SERVER'), getenv('MAIL_PORT'), context=context) as smtp:
            smtp.login(getenv('MAIL_USERNAME'), getenv('MAIL_PASSWORD'))
            smtp.sendmail(getenv('MAIL_USERNAME'), email, em.as_string())
            smtp.quit()
    except smtplib.SMTPConnectError as e:
        return e

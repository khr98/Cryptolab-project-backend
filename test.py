import smtplib, ssl

SMTP_SSL_PORT=465 # SSL connection
SMTP_SERVER="smtp.gmail.com"

SENDER_EMAIL="hyerim980513@gmail.com"
SENDER_PASSWORD="ynazvzwuyqzeatql"

RECEIVER_EMAIL="colorstar28@gmail.com"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_SSL_PORT, context=context) as server:
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, "sending SMTP email test")

import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "mmw.creator@gmail.com"
password = "faxdnlpyraebmbcz"

receiver = "mmw.creator@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Test
This is a test email

Thanks.
"""

with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
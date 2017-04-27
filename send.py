# This file is used to send the email out.

from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

def send():
    if Config.testing:
        print('send')
    else:
        msg = MIMEMultipart()

        with open('text.txt', 'r') as fp:
            msg = MIMEText(fp.read())

        msg['Subject'] = Config.subject
        msg['From'] = Config.sender
        msg['To'] = Config.receivers

        try:
            smtp_obj = SMTP(Config.server, Config.port)
            smtp_obj.sendmail(Config.sender, Config.receivers, msg)
            print('Successfully sent email')
        except SMTPException:
            print('Error: unable to send email')
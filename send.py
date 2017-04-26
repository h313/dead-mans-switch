# This file is used to send the email out.

from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = 'mail.your-domain.com'
port = 25
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
subject = 'dead mans switch'


def send():
    msg = MIMEMultipart()

    with open('text.txt', 'r') as fp:
        msg = MIMEText(fp.read())

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers

    try:
        smtp_obj = SMTP(server, port)
        smtp_obj.sendmail(sender, receivers, msg)
        print('Successfully sent email')
    except SMTPException:
        print('Error: unable to send email')
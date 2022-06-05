import constants as CON
import smtplib
import re
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Notify:
    def __init__(self):
        self.sender_account = CON.EMAIL
        self.sender_username = CON.EMAIL
        self.sender_password = CON.PASSWORD
        self.smtp_server = CON.SMTP_SERVER
        self.smtp_port = CON.SMTP_PORT
        self.report_subject = 'Temperature Report {}'.format(dt.datetime.now().replace(microsecond=0))
        self.warning_subject = 'WARNING! Temperature Alert {}'.format(dt.datetime.now().replace(microsecond=0))
        self.email_recipients = {'Maximilian Groening': 'maximilian.groening@haw-hamburg.de',
                                 'Bjoern Hoefer': 'bjoern.hoefer@haw-hamburg.de'}

    def update_contacts(self):
        # get new mail addresses
        raw_input = input('Enter email to receive notifications: \n'
                          '(separate different addresses with a ";" \n'
                          '\n')
        contact_list = raw_input.replace(" ", "").split(';')
        # check if mail
        checked_contacts = {}
        pat = "^[\w\.\+\-]+\@[\w\.\+\-]+\.[a-z]{2,3}$"
        for mail in contact_list:
            if re.match(pat, mail):
                name = mail.split("@")[0].replace(".", " ")
                checked_contacts[name] = mail
            else:
                continue
        self.email_recipients = checked_contacts

    def send_report(self):
        # login to email server
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_username, self.sender_password)
        # For loop, sending emails to all email recipients
        for name, recipient in enumerate(self.email_recipients):
            print(f"Sending email to {recipient}")
            message = MIMEMultipart('alternative')
            message['From'] = self.sender_account
            message['To'] = recipient
            message['Subject'] = self.report_subject
            message.attach(MIMEText(
                '<p>Hallo {},</p>' \
                '<p>hier ist der monatliche Bericht deines PiHeat.</p>' \
                '<p>Sch&ouml;nen Tag (:</p>'.format(name)
                , 'html'))
            text = message.as_string()
            server.sendmail(self.sender_account, recipient, text)
        # All emails sent, log out.
        server.quit()

    def send_warning(self):
        # login to email server
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_username, self.sender_password)
        # For loop, sending emails to all email recipients
        for name, recipient in enumerate(self.email_recipients):
            print(f"Sending email to {recipient}")
            message = MIMEMultipart('alternative')
            message['From'] = self.sender_account
            message['To'] = recipient
            message['Subject'] = self.warning_subject
            message.attach(MIMEText(
                '<p>Hallo {},</p>' \
                '<p>hier ist der monatliche Bericht deines PiHeat.</p>' \
                '<p>Sch&ouml;nen Tag (:</p>'.format(name)
                , 'html'))
            text = message.as_string()
            server.sendmail(self.sender_account, recipient, text)
        # All emails sent, log out.
        server.quit()

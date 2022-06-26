import constants as CON
import smtplib
import re
import datetime as dt
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



class ControlNotify:
    def __init__(self):
        self.sender_account = CON.EMAIL
        self.sender_username = CON.EMAIL
        self.sender_password = CON.PASSWORD
        self.smtp_server = CON.SMTP_SERVER
        self.smtp_port = CON.SMTP_PORT
        self.report_subject = 'Temperature Report {}'.format(dt.datetime.now().replace(microsecond=0))
        self.warning_subject = 'WARNING! Temperature Alert {}'.format(dt.datetime.now().replace(microsecond=0))
        self.email_recipients = {#'Lennard Rüdiger Voigt': 'lennardvoigt@hotmail.de',
                                 #'Julian Katz': 'julian.katz@haw-hamburg.de',
                                 'Maximilian Groening': 'maximilian.groening@haw-hamburg.de',
                                 'Bjoern Hoefer': 'bjoern.hoefer@haw-hamburg.de',
                                 }

    def update_contacts(self):
        # get new mail addresses
        raw_input = input('Enter email to receive notifications: \n'
                          '(separate different addresses with a ";") \n'
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

    def send_report(self, plot_path):
        # login to email server
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_username, self.sender_password)
        # For loop, sending emails to all email recipients
        for name in self.email_recipients:
            print(f"Sending email to {name}")
            message_root = MIMEMultipart('alternative')
            message_root['From'] = self.sender_account
            message_root['To'] = self.email_recipients[name]
            message_root['Subject'] = self.report_subject
            message_root.attach(MIMEText(
                '<p>Hallo {},</p>'
                '<p>hier ist der monatliche Bericht deines PiHeat.</p>'
                '<img src="cid:image1" alt="Plot" width="1500" height="1500">'
                '<p>Hab einen sch&ouml;nen Tag (:</p>'.format(name)
                , 'html'))
            # Attach Image
            fp = open(plot_path, 'rb')  # Read image
            msg_image = MIMEImage(fp.read())
            fp.close()
            # Define the image's ID as referenced above
            msg_image.add_header('Content-ID', '<image1>')
            message_root.attach(msg_image)
            server.sendmail(self.sender_account, self.email_recipients[name], message_root.as_string())
        # All emails sent, log out.
        server.quit()

    def send_warning(self, critical_temp):
        # login to email server
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_username, self.sender_password)
        # For loop, sending emails to all email recipients
        for name in self.email_recipients:
            print(f"Sending email to {name}")
            message = MIMEMultipart('alternative')
            message['From'] = self.sender_account
            message['To'] = self.email_recipients[name]
            message['Subject'] = self.warning_subject
            message.attach(MIMEText(
                '<p><b>!!! WARNUNG !!!</b></p>'\
                '<p>Hallo {},</p>'\
                '<p></p>'\
                '<p><strong>deine Kacke ist grade so richtig am dampfen!</strong></p>'\
                '<p>Wir haben eine zu hohe Temperatur ({} C°) festgestellt</p>'\
                '<p></p>'\
                '<p>Bitte überprüfe <b>sofort</b> deinen Stuhl</p>'\
                '<p></p>'\
                '<p>Sch&ouml;nen Tag (:</p>'.format(name, critical_temp)
                , 'html'))
            text = message.as_string()
            server.sendmail(self.sender_account, self.email_recipients[name], text)
        # All emails sent, log out.
        server.quit()

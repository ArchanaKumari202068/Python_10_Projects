# go over to gmail account and setup 2 factor authentication
# generate app password
# create a function to send the mail
#bayxxotpfbhckzrm     securesally@gmail.com


from email.message import EmailMessage
from app2 import password
import ssl
import smtplib



email_sender = 'archanakumari202068@gmail.com'
email_password = password #security 
email_receiver = 'yilare5389@areosur.com'
subject = "Testing"
body = """
Waiting for your reply...
"""

em = EmailMessage() #instance 
em['from'] = email_sender
em['To'] = email_receiver
em['subjects'] = subject
em.set_content(body)
context = ssl.create_default_context ()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())


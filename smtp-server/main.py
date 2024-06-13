#Sending Email Script
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
# to load from env
load_dotenv()
################################
################################
# HEADS-UP you need the .env file that I explained in the YouTube video
################################
################################

frm = os.getenv('MYEMAIL')
recv = os.getenv('DESTEMAIL')
passwd = os.getenv("PASSWORD")
subject = 'HELLO THERE!'
body = "What's up?"

msg = MIMEText(body)
msg['From'] = frm
msg['To'] = recv
msg['Subject'] = subject

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(frm,passwd)
server.sendmail(frm,recv, msg.as_string())
server.quit()

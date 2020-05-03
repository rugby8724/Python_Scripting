import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'J W'
email['to'] = 'jeremiah.d.wise@gmail.com'
email['subject'] = 'Zero to Mastery Python'

email.set_content(html.substitute(name = 'TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jeremiah.d.wise@gmail.com', 'testing1234')
    smtp.send_message(email)
    print('all good boss!')

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()

text = Template(Path('/Users/ramsaiteja/Downloads/PYTHON PROGRAMS/pythonemail/new.html').read_text())



email['from'] = 'amanbhaaai'
email['to'] = 'others_mail_id'
email['subject'] = 'Aman bhaaaaai '
email.set_content(text.substitute({'name' :'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_mail_id','your_mail_password')
    smtp.send_message(email)
    print('mail sent!!!')



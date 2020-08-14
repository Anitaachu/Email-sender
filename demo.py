 import os
import smtplib

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(EMAIL_USER, EMAIL_PASSWORD)
message = subject = 'Grab dinner this weekend?'
body = 'How about dinner with me tonight'
msg = f'Subject: {subject}\n\n{body}'
server.sendmail(EMAIL_USER,'anitatom20@gmail.com', msg)
server.quit()
print("Email sent!")

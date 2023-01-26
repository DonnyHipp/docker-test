import smtplib

from email.message import EmailMessage


SERVER = "pmi-com.mail.protection.outlook.com"

FROM = "iLearn@app.pmi"

TO = ["igor.toloknov@contracted.pmi.com"] # must be a list

# Open the plain text file whose name is in textfile for reading.

msg = EmailMessage()

msg['Subject'] = 'Test Message from iLearn'
msg['From'] = FROM
msg['To'] = ', '.join(TO)

msg.set_content("""\

Hello,

this is test message from iLearn system

--Robo

""")


# Send the message via our own SMTP server.

s = smtplib.SMTP(SERVER,25)
s.send_message(msg)
s.quit()
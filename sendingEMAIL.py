#!/usr/bin/python
def send_mail(message):

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    username = "sender@outlook.com"
    password = "sender's password"

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('sending mail to ' + recipient + ' on ' + subject)

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

    except error as e:
        print(str(e))


def getError():
	res=''
	path = os.path.join(os.path.expanduser('~'), 'attack-engine1', 'outputFiles', 'Error.txt')
	with open (path,'w') as f:
		res += f.readlines()
	return res

Message=getError()
send_email(message)

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_email():

    sender = 'maze.arduino@gmail.com'
    passwd = '123Soleil!,'
    receiver = 't.mazaleyrat@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Alert Free Spot'

    body = 'Hi Julie,\n\nnew spots are available.\n\nThis is Dope\n\nRegards,\n\nArduino'
    msg.attach(MIMEText(body))

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(sender, passwd)
    mailserver.sendmail(sender, receiver, msg.as_string())
    mailserver.quit()

if __name__ == '__main__':
    send_email()
    print 'caca'

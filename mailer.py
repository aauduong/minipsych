import smtplib

from email.mime.text import MIMEtext

with open(sys.argv[1]) as fp:
	msg = MIMEtext(fp.read)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = 'aauduong@berkeley.edu'
msg['To'] = 'aauduong@berkeley.edu'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

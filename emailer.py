import pyzmail

# Initial configuration for sending mail:
def send_mail (recipient, subject, body):
	sender=(u'Me', 'auduongalicia@gmail.com')
	recipients=[(u'Him', recipient), recipient]
	subject=subject
	text_content=body
	prefered_encoding='iso-8859-1'
	text_encoding='iso-8859-1'
	payload, mail_from, rcpt_to, msg_id=pyzmail.compose_mail(
	        sender,  recipients, 
	        subject, prefered_encoding,  (text_content, text_encoding), 
	        html=None, 
	        attachments=[('attached content', 'text', 'plain', 'text.txt',
	                      'us-ascii')])

	smtp_host='smtp.gmail.com'
	smtp_port=587
	smtp_mode='tls'
	smtp_login='auduongalicia@gmail.com'
	smtp_password='_________'

	ret=pyzmail.send_mail(payload, mail_from, rcpt_to, smtp_host, \
	        smtp_port=smtp_port, smtp_mode=smtp_mode, \
	        smtp_login=smtp_login, smtp_password=smtp_password)

	if isinstance(ret, dict):
	    if ret:
	        print('failed recipients:', ', '.join(ret.keys()))
	    else:
	        print('success')
	else:
	    print('error:', ret)

def send_mail_periodic():
	# Have a list of emails. Open it and send emails to certain emails at regular intervals
	# might be useful just to keep a list of (email_address, Times) tuples. When you send an email,
	# you could update the time by ~1 week.

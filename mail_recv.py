import poplib
from email import parser

def mail_receiver (mail_arr):
	# This was copied from the internet.
	# Make 
	pop_conn = poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user('auduongalicia')
	pop_conn.pass_('________')
	#Get messages from server:
	messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
	# Concat message pieces:
	messages = ["\n".join(msg[1]) for msg in messages]
	mail_file = open("client_name", "w")
	json.dump(messages, mail_file)
	mail_file.close()
	#Parse message intom an email object:
	#messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	#for message in messages:
	 #   print message['subject']
	#pop_conn.quit()

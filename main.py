import emailer
import minipsych
import mail_recv
import multiprocessing

#save into json
#json.parse +++> dictionary => read
#parse return emails

received_email = []

threads = []
# Make it so you can pass the received_email list into these thread_starts.
# Just google the multiprocessing library and it should be apparent.
threads.append(multiprocessing.Process(target=mail_recv.mail_receiver))
threads.append(multiprocessing.Process(target=emailer.send_mail_periodic))
threads.append(multiprocessing.Process(target=mail_recv.mail_receiver))
p.start()

for thread in threads:
	thread.start()


mail_recv.py
#send
#recieve
#log
#deveiopslingshot for relaying
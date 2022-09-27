import smtplib
import mimetypes
from email.message import EmailMessage
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os


year = datetime.now().strftime("%Y")
month = datetime.now().strftime("%m-%Y")
path1 = '/home/pi/Desktop/Birdwatcher'
path2 = '/home/pi/Desktop/Birdwatcher/%s' %year
path3 = '/home/pi/Desktop/Birdwatcher/%s/%s' % (year, month)
        

try:
    os.mkdir(path1)
except OSError as error:
    print(error)
try:
    os.mkdir(path2)
except OSError as error:
    print(error)
try:
    os.mkdir(path3)
except OSError as error:
    print(error)



time = datetime.now(  ).strftime("%d-%m-%Y_%H-%M")

camera = PiCamera()
#camera.rotation =180
camera.start_preview()



sleep(2)
camera.capture('%s/image_%s.jpg' %( path3, time)) 
camera.stop_preview()



# E-Mail-Objekt initialisieren und Nachrichtentext setzen:
msg = EmailMessage()
msg['Subject'] = 'Vogelbeobachtung'
msg['From'] = 'fsr-ing@fh-asta.de'
msg['To'] = 'falk.kallmer@gmail.com'
# Set text content
msg.set_content('Hallo, \n Foto befindet sich im Anhang!')

def attach_file_to_email(email, filename):
    """Attach a file identified by filename, to an email message"""
    with open(filename, 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/")
        email.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)

# Anhang anhängen
attach_file_to_email(msg, "%s/image_%s.jpg" %( path3, time))

def send_mail_smtp(mail, host, username, password):
    s = smtplib.SMTP(host)
    s.starttls()
    s.login(username, password)
    s.send_message(mail)
    s.quit()

# E-Mail per SMTP senden
send_mail_smtp(msg, 'mail.tiggerswelt.net', 'fhasta_fsr-ing', '!ng3n!3ur5r%')
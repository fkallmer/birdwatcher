import smtplib
import mimetypes
from email.message import EmailMessage
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os
import logging
from folder import *

class mail():     

    def sendMail(pSubject, pFrom, pTo, pContent, pFile, filename, host, username, password):
   # def __init__():
       # logging.basicConfig(filename="mai.log.txt", format="%(asctime)s %(message)s")
        folder.compress(pFile)
        pZip = pFile + '.zip'
        print(pFile)
        msg = EmailMessage()
        msg['Subject'] = pSubject
        msg['From'] = pFrom
        msg['To'] = pTo
        msg.set_content(pContent) # Inhalt der Mail
            
        try:
            with open(pZip, 'rb') as fp:
                file_data = fp.read()
                maintype, _, subtype = (mimetypes.guess_type(pZip)[0] or 'application/octet-stream').partition("/")
                msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)
                
        except Exception as e:
            logging.error(e)
                
        try:
            s = smtplib.SMTP(host)
            s.starttls()
            s.login(username, password)
            s.send_message(msg)
            s.quit()
            folder.delFolder(pFile)
            os.remove(pZip)
        except Exception as e:
            logging.error(e)
            
            
            
            
            


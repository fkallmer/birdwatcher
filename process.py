from datetime import datetime
from folder import *
from camera import *
from mail import *
import logging

class Process():
        
    class __init__():
        
        time = datetime.now(  ).strftime("%d-%m-%Y_%H-%M-%S")
        year = datetime.now().strftime("%Y")
        month = datetime.now().strftime("%m-%Y")
        path1 = '/home/pi/Desktop/Birdwatcher'
        path2 = '/home/pi/Desktop/Birdwatcher/%s' %year
        path3 = '/home/pi/Desktop/Birdwatcher/%s/%s' % (year, month)
        pFile = path3 +'/image_'+ time + '.jpg'
        filename = time 
        
        pSubject = 'Vogelbeobachtung ' + time
        pFrom = [MAILADRESSE-VON]
        pTo = [MAILADRESSE-ZU]
        pContent = [MAILINHALT]
        host = [SMTP-URL]
        username = [BENUTZERNAME]
        password = [PASSWORT]
        
        pTransfer = '/home/pi/Desktop/Birdwatcher/transfer'
        logging.basicConfig(filename="process_log.txt", format="%(asctime)s %(message)s")
            
        #folder.delFolder('/home/pi/Desktop/Birdwatcher'     
        folder.createFolder(path1)
        folder.createFolder(path2)
        folder.createFolder(path3)
        folder.createFolder(pTransfer)
             
        camera.takePhoto(pFile)
                
        folder.transfer(pFile, pTransfer)
                
        mail.sendMail(pSubject, pFrom, pTo, pContent, pTransfer, filename, host, username, password)
       
            
        

        
        



from datetime import datetime # Import Datetime-Bibliothek, für den Umgang mit Daten und Zeiten
from folder import * # Import folder.py
from camera import * # Import camera.py
from transfer import * #Import transfer.py
import logging # Import Logging-Bibliothek zum Erstellen einer Logdatei

class Process():
        
    class __init__(): # Ausführung beim Programmaufruf
                                                                                                        # DD-MM-YYYY_HH-MM-SS
        time = datetime.now(  ).strftime("%d-%m-%Y_%H-%M-%S") # Erstellung der aktuell Uhrzeit im Format "03-10-2022_20-13-23"
        year = datetime.now().strftime("%Y") # Erstellung des Jahres als Text
        month = datetime.now().strftime("%m-%Y") # Erstellung des Monates und Jahres als Text
        path1 = '/home/pi/Desktop/Birdwatcher' # Ordnerpfad 1
        path2 = '/home/pi/Desktop/Birdwatcher/%s' %year #Ordnerpfad 2
        path3 = '/home/pi/Desktop/Birdwatcher/%s/%s' % (year, month) # Ordnerpfad 3
        pFile = path3 +'/image_'+ time + '.jpg' #Dateipfad für die Aufnahme
        filename = time # Dateiname für den Mail-Versand
        
        pSubject = 'Vogelbeobachtung ' + time # Betreff der E-Mail
        pFrom = [MAILADRESSE-VON] # Absenderadresse der Mail [zu ergänzen]
        pTo = [MAILADRESSE-ZU] # Empfaengeradresse [zu ergänzen]
        pContent = [MAILINHALT] # E-Mailtext [zu ergänzen]
        host = [SMTP-URL] # SMTP-Url des Mailproviders [zu ergänzen]
        username = [BENUTZERNAME] # Benutzername des Mail-Kontos
        password = [PASSWORT] # Passwort des Mail-Kontos
        
        pTransfer = '/home/pi/Desktop/Birdwatcher/transfer' # Ordnerpfad für den Transferordner
        logging.basicConfig(filename="process_log.txt", format="%(asctime)s %(message)s") # Erstellung und Konfiguration der Log-Datei
            
        #folder.delFolder('/home/pi/Desktop/Birdwatcher'     
        folder.createFolder(path1) # Erstellung des Orners an Pfad 1
        folder.createFolder(path2) # Erstellung des Orners an Pfad 2
        folder.createFolder(path3) # Erstellung des Orners an Pfad 3
        folder.createFolder(pTransfer) # Erstellung des Transferordners
             
        camera.takePhoto(pFile) # Aufnahme und Speicherung unter dem Dateipfad
                
        folder.transfer(pFile, pTransfer) # Kopieren der Aufnahme in den Transferordner
                
        transfer.sendMail(pSubject, pFrom, pTo, pContent, pTransfer, filename, host, username, password) # Versand der Datei per E-Mail in einer .zip-Datei
       
            
        

        
        



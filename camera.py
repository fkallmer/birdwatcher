from picamera import PiCamera
import logging
from time import sleep

class camera():
    
    def takePhoto(pFile):
    
        try:
            camera = PiCamera()
            camera.rotation =180
            camera.start_preview()
            sleep(2)
            camera.capture(pFile) 
            camera.stop_preview()
        except Exception as a:
            logging.error(a)
        
    
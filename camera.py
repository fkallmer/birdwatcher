from picamera import PiCamera
from datetime import datetime
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



time = datetime.now(  ).strftime("%d-%m-%Y_%H-%M-%S")

camera = PiCamera()
#camera.rotation =180
camera.start_preview()


for i in range (0,10):
    time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    sleep(2)
    camera.capture('%s/image_%s.jpg' %( path3, time)) 
camera.stop_preview()
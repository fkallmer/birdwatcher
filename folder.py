import os
from datetime import datetime

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

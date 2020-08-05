import requests
from datetime import datetime
import time
import random

def send (obj, url):
    myobj = {'from': "Station: {}; Sensor: {}".format(obj.id, obj.sensorId), 'temp': obj.temp, 'pres': obj.presure, 'hum': obj.humidity, 'batV': obj.batV, 'RSSI': obj.RSSI, 'date_received':datetime.now().strftime("%m.%d.%Y %H:%M:%S")}
    return requests.post(url, data=myobj)
"""for i in range (5):
    requests.post('http://192.168.88.224:5000',data={'from':'otherCom','temp':random.randint(15, 40),'pres':random.randint(900, 1400),'hum':random.randint(0, 100),'batV':4.981,'RSSI':-21,'date_received':datetime.now().strftime("%m.%d.%Y %H:%M:%S")})
    time.sleep(5)    """


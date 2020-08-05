import serial
import serial.tools.list_ports
import time
import Pomiar
import datetime
import do_wysylanie

# variables
file_name = 'Data_ws.txt'
StaionId = 'MAIN'
url = 'https://flasktestws.herokuapp.com'

# port
ports = serial.tools.list_ports.comports()
port = ports[0]
port = port.device

ser = serial.Serial(port, 9600)


# get data arduino -> Raspberry
def get_data_serial():
    line = ser.readline()
    line = line.decode()
    line = line.rstrip()
    line_data = [float(x) for x in line.split()]
    pomiar = Pomiar.Pomiar(StaionId ,line_data)
    return pomiar


#main core
def main_core():
    ser.readline()
    while True:
        pm = get_data_serial()
        do_wysylanie.send(pm, url)
        time.sleep(1)


main_core()

class Pomiar ():

    def __init__ (self, id, measure):
        self.id = id
        self.sensorId = measure[0]
        self.temp = measure[1]
        self.presure = measure[2]
        self.humidity = measure[3]
        self.batV = measure[4]
        self.RSSI = measure[4]

    def __repr__ (self):
        return (repr((self.id, self.sensorId, self.temp, self.presure, self.humidity, self.batV, self.RSSI)))





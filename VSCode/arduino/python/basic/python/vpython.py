import serial

arduinoSeiralData = serial.Serial('com4', 9600)

while(True):
    if (arduinoSeiralData.inWaiting() > 0):
        mydata = arduinoSeiralData.readline()
        cnt = float(mydata)
        print(cnt)


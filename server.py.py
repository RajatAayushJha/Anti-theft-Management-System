import serial #import Serial
import time

CCSerial = serial.Serial('com7', 115200)
time.sleep(2)
while(1):
	CCSerial.write('0'.encode('utf-8'))
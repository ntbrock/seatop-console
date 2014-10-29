#!/usr/bin/python

#http://raspberrypi.stackexchange.com/questions/13930/capturing-serial-number-of-2-usb-rfid-reader-in-python-pi2-rfid-mifire-rfid

import serial
import sys

if len(sys.argv) < 2:
  print "Usage: cat_serial USBtty<n> (0 is usually GPS, 1 is NX2)"
  sys.exit(-1)


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


port = '/dev/ttyUSB' + sys.argv[1]
baud = 4800 # NMEA
timeout = 10

ser = serial.Serial(port=port, baudrate=baud, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=timeout)


while True:
    try:
        response = ser.readline()
        print response.rstrip()
    except KeyboardInterrupt:
        break

ser.close()


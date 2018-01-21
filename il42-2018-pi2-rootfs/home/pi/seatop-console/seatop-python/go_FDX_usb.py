#!/usr/bin/python
# 2015-Mar-01 - Upgrade to support SIGHUP to insert the current unix time into the NMEA stream as a meta line

#http://raspberrypi.stackexchange.com/questions/13930/capturing-serial-number-of-2-usb-rfid-reader-in-python-pi2-rfid-mifire-rfid

import signal, os
import serial, select
import sys
import time

if len(sys.argv) < 3:
  print "Usage: cat_FDX USBtty<n> <baud> (0 is usually GPS, 1 is NX2, FDX is 19200, Arduino is 9600)"
  sys.exit(-1)


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

port = '/dev/ttyUSB' + sys.argv[1]

if sys.argv[1] == 'A':
  port = '/dev/ttyACM0'

#baud = 4800 # NMEA

# FDX
#baud = 19200
baud = int(sys.argv[2])


#baud = 115200
timeout = 10

ser = serial.Serial(port=port, baudrate=baud, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=timeout)

printAlignmentMetadata = 1

# ---- signal handling -----------------------------
# man 7 signal :  SIGUSR1   30,10,16    Term    User-defined signal 1
# accept SIGUSR1 to add unix timestamp + metadata to the setup
# https://docs.python.org/2/library/signal.html
def handler(signum, frame):
  # print "I am in handler: {0}".format(signum)
  # re-register
  signal.signal(signal.SIGUSR1, handler)

  global printAlignmentMetadata
  if signum == signal.SIGUSR1:
    printAlignmentMetadata = 1

# Initial registration
signal.signal(signal.SIGUSR1, handler)
# --------------------------------------------------

print "# Going FDX mode with : $PSILFDX,,R"

ser.write("$PSILFDX,,R\r\n")


ser.close()

#!/usr/bin/python
# 2015-Mar-01 - Upgrade to support SIGHUP to insert the current unix time into the NMEA stream as a meta line
# 2015-Mar-01 - Clone of cat, also tees information out to graphite.

#http://raspberrypi.stackexchange.com/questions/13930/capturing-serial-number-of-2-usb-rfid-reader-in-python-pi2-rfid-mifire-rfid

import signal, os
import serial, select
import sys
import time
import graphitesend

if len(sys.argv) < 2:
  print "Usage: cat_serial USBtty<n> (0 is usually GPS, 1 is NX2)"
  sys.exit(-1)


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

port = '/dev/ttyUSB' + sys.argv[1]
baud = 4800 # NMEA
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

# ---- graphite delivery -----------------------------
# https://github.com/daniellawrence/graphitesend
g = graphitesend.init(prefix='seatop', dryRun=True) # use hostname

# --------------------------------------------------

print "# start, unixTime, {0}, -------------------------------------".format(time.time())
while True:
    try:
        response = ser.readline()
        print response.rstrip()

        # CSV parse the file, send metrics to graphite
        s = response.split(',')
        noun = s[0]
        d = { "#{0}_count".format: 1 }

        ## TODO, get an IDX dictionary for synonum,s the number offets are too clumsy
        for idx, val in enumerate(s):
          d["#{0}_#{idx}"] = val
       
        g.send_dict(d)
        #----------------------------------------

        if printAlignmentMetadata:
          print "# timestamp, unixTime, {0}, -------------------------------------".format(time.time())
          printAlignmentMetadata = 0
    except select.error as ex:
      # handle SIGUSR1 interrupting the serial select
      print "# error, select.error, {0}".format(ex)

    except KeyboardInterrupt:
      break

ser.close()

print "# stop, unixTime, {0}, -------------------------------------".format(time.time())

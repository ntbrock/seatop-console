#!/usr/bin/python

# set_unix_time from Gps - SeaTop
# 2015-Mar-01 Brockman - Set the pi date via a sudo date command by finding the first GPS RMC sentence off a configurable usb tty
# 2015-Mar-05 Brockman - Added support for previous 24 hours of lemons gps with sentence: $GPZDA,025058.000,04,03,2015,00,00*5D

import serial
import sys
import re
from subprocess import call
import signal, os

# Set the signal handler and a 30-second alarm
# signal.signal(signal.SIGALRM, handler)
signal.alarm(30)


if len(sys.argv) < 2:
  print "Usage: set_unix_time_from_gps.py USBtty<n> (0 is usually GPS, 1 is NX2)"
  sys.exit(-1)


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)


port = '/dev/ttyUSB' + sys.argv[1]
baud = 4800 # NMEA
timeout = 10

ser = serial.Serial(port=port, baudrate=baud, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=timeout)

maxAttempts = 100
attempt = 0

while attempt < maxAttempts:

    attempt += 1


    try:
        raw_response = ser.readline()
        response = raw_response.rstrip()

        # Sample GPRMC line to assist with regex creation
        # $GPRMC,133838.075,A,3249.4824,N,07951.5244,W,,,010315,,,N*69
        # REQUIRE Active RMC, skip the voids

        # Parse the line via simple regex to minimize library dependency
        m = re.search('^\$GPRMC,([0-9]{2})([0-9]{2})([0-9]{2})[.0-9]{4},A,.*?,([0-9]{2})([0-9]{2})([0-9]{2}),', response)
        if m:
          # print "Matches: {0}".format(m)


          utc_HH = m.group(1)
          utc_MM = m.group(2)
          utc_SS = m.group(3)

          date_DD = m.group(4)
          date_MM = m.group(5)
          date_YY = m.group(6)

          utcTimeStr = "{0}:{1}:{2}".format(utc_HH, utc_MM, utc_SS)
          dateStr = "{0}-{1}-{2}".format(date_YY, date_MM, date_DD)
          fullStr = "{0} {1}".format(dateStr, utcTimeStr)

          # execute the system date command
          print "GPRMC Date Set: {0}    UTC Time: {1}   Date: {2}".format(fullStr, utcTimeStr, dateStr)
          call(["sudo", "date", "-u", "-s", "{0}".format(fullStr), "+%F %T"])

          # finish execution
          ser.close()
          sys.exit(0)


        # 2015-Mar-05 New sentence from lemons gps: $GPZDA,025058.000,04,03,2015,00,00*5D
        # Parse the line via simple regex to minimize library dependency
        # pardon the Y2100K bug ;) See you in heaven
        m = re.search('^\$GPZDA,([0-9]{2})([0-9]{2})([0-9]{2})[.0-9]{3},([0-9]{2}),([0-9]{2}),20([0-9]{2}),', response)
        if m:

          utc_HH = m.group(1)
          utc_MM = m.group(2)
          utc_SS = m.group(3)

          date_DD = m.group(4)
          date_MM = m.group(5)
          date_YY = m.group(6)

          utcTimeStr = "{0}:{1}:{2}".format(utc_HH, utc_MM, utc_SS)
          dateStr = "{0}-{1}-{2}".format(date_YY, date_MM, date_DD)
          fullStr = "{0} {1}".format(dateStr, utcTimeStr)

          # execute the system date command
          print "GPZDA Date Set: {0}    UTC Time: {1}   Date: {2}".format(fullStr, utcTimeStr, dateStr)
          call(["sudo", "date", "-u", "-s", "{0}".format(fullStr), "+%F %T"])

          # finish execution
          ser.close()
          sys.exit(0)

        print response
    except KeyboardInterrupt:
        break

ser.close()

print "ERROR: Failed after {0} attempts to find a GPS 'RMC' Sentence with Active, Non-void status".format(attempts)
 

#!/usr/bin/env python

# Simple NMEA generator that posts via tcp to localhost kplex
# for use in determining how the nexus will handle the 
 

## In Nexus Server, to override the nx2 log and instead use nmea log, set C73 = off

# From NX2 Control Manual: http://static.garmin.com/pumac/NX2-Multi-contol-eng.pdf
# 12.6.4 C73 (OFF BSP)
# (OFF) = NX2 log transducer. (On) = NMEA log transducer.
# If you want to use a NMEA transducer (connected to the NMEA input, you have to set
# C73 to On. The Server will then transmit this information on the Nexus Network to all
# connected instruments.
# After you have changed this setting, you have to restart the system 




import socket
import time
 
TCP_IP = '127.0.0.1'
TCP_PORT = 10110
BUFFER_SIZE = 1024


#-----------------------------------------------------
# checksummer
# http://code.activestate.com/recipes/576789-nmea-sentence-checksum/

import re

""" Calculate  the checksum for NMEA sentence 
    from a GPS device. An NMEA sentence comprises
    a number of comma separated fields followed by
    a checksum (in hex) after a "*". An example
    of NMEA sentence with a correct checksum (of
    0x76) is:
    
      GPGSV,3,3,10,26,37,134,00,29,25,136,00*76"
"""

def checksum(sentence):

    """ Remove any newlines """
    if re.search("\n$", sentence):
        sentence = sentence[:-1]

    nmeadata,cksum = re.split('\*', sentence)

    calc_cksum = 0
    for s in nmeadata:
        calc_cksum ^= ord(s)

    """ Return the nmeadata, the checksum from
        sentence, and the calculated checksum
    """
    return nmeadata,'0x'+cksum,hex(calc_cksum)


##--------------------------------------------------
#main 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)

for hdt in range(360):
 
  hdtp = format(hdt, "03d")
  hdmp = format(hdt+7, "03d")
  bsp = format(hdt/10, "0.2f") 

 
  MESSAGE = f"IIVHW,{hdtp},T,{hdmp},M,11.11,N,{bsp},K*00"

  data,cksum,calc_cksum = checksum(MESSAGE)
  last2 = calc_cksum[-2:]

  s.send(("$"+data+"*"+last2+"\r\n").encode())

# s.send(MESSAGE.encode())

  print(f"sent data: {data}*{last2} cksum: {cksum} calc_cksum: {calc_cksum}\r\n")

  ## Message 1 - temperature

  MESSAGE1 = f"IIMTW,20,C*00"
  data1,cksum1,calc_cksum1 = checksum(MESSAGE1)
  last21 = calc_cksum1[-2:]
  s.send(("$"+data1+"\r\n").encode())
  print(f"sent msg1: {data1} cksum: {cksum1} calc_cksum: {calc_cksum1}\r\n")




  ## Message 2 - Custom target speed

  MESSAGE2 = f"PSILTBS,{bsp},N*00"
  data2,cksum2,calc_cksum2 = checksum(MESSAGE2)
  last22 = calc_cksum2[-2:]
  s.send(("$"+data2+"*"+last22+"\r\n").encode())
  print(f"sent msg2: {data2}*{last22} cksum: {cksum2} calc_cksum: {calc_cksum2}\r\n")

  ## Message 3 - Custom Angles

  MESSAGE3 = f"PSILCD1,{hdtp}.4,{hdtp}.6,*00"
  data3,cksum3,calc_cksum3 = checksum(MESSAGE3)
  last23 = calc_cksum3[-2:]
  s.send(("$"+data3+"*"+last23+"\r\n").encode())
  print(f"sent msg3: {data3}*{last23} cksum: {cksum3} calc_cksum: {calc_cksum3}\r\n")

  time.sleep(1) 



#data = s.recv(BUFFER_SIZE)

s.close()

#print("received data:", data)



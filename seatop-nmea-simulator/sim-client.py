#!/usr/bin/env python
 
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
  o = 100
 
  MESSAGE = "IIVHW,"+hdtp+",T,331,M,02.22,N,03.33,K*00"

#  MESSAGE = f"IIVHW,{hdtp},T,331,M,02.22,N,03.33,K*00"

  data,cksum,calc_cksum = checksum(MESSAGE)
  last2 = calc_cksum[-2:]

  s.send(("$"+data+"*"+last2+"\r\n").encode())

# s.send(MESSAGE.encode())

  print("sent data: "+data+"*"+last2+" cksum: "+cksum+" calc_cksum: "+calc_cksum+"\r\n")

  time.sleep(1) 



#data = s.recv(BUFFER_SIZE)

s.close()

#print("received data:", data)



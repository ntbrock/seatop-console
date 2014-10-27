#!/usr/bin/python
# Seatop lives!  This reads nx2 log files and writes them into the mysql database

import re
import sys
import csv
import pynmea2
from pprint import pprint
from datetime import date, datetime, timedelta
from geopy.point import Point

nmeaDict = {
    "XTE" : "Cross Track Error",
    "WCV" : "Waypoint Velocity",
    "HDT" : "Heading True", # <HDT(heading=Decimal('261'), hdg_true='T')>
    "HDM" : "Heading Magnetic",
    "MWD" : "Measured Wind Direction", # <MWD(direction_true=Decimal('231.14'), true='T', direction_magnetic=Decimal('238.44'), magnetic='M', wind_speed_knots=Decimal('4.35'), knots='N', wind_speed_meters=Decimal('2.24'), meters='M')>
    "VHW" : "Velocity Headway", # <VHW(heading_true=Decimal('261'), true='T', heading_magnetic=Decimal('268'), magnetic='M', water_speed_knots=Decimal('6.46'), knots='N', water_speed_km=Decimal('11.96'), kilometers='K')> 
    "DBT" : "Depth Below Transducer",
    "GLL" : "GPS Position LatLon",
    "GSV" : "GPS Sattelites in View",
    "ZDA" : "GPS Date Time",
    "VTG" : "Velocity Over Ground",
    "MWV" : "Measured Wind Velocity"
}



if len(sys.argv) < 3:
    print "Usage: ingress_nx2.py <captureDate YYYY-MM-DD> <nx2LogFilename>"
    sys.exit(-1)

readDate = datetime.strptime(sys.argv[1], "%Y-%m-%d")
readFilename = sys.argv[2]

lastDatestamp = readDate
lastTimestamp = None ## dont' accept rows until we get the first datestamp
lastLat = None
lastLon = None
lastPoint = None ## Only accept until we get first gps reading

# Read the incoming nexus file
readf = open( readFilename, "r" )
for lineRaw in readf:
  line = lineRaw.rstrip()

  ## Provide filtering OUT until I contribute new sentence types back to pynmea2
  if re.match('^\$II(VPW|VWT|VDR)',line):
    # do not parse line
    1

  else: 

    msg = pynmea2.parse(line)
    print "Message: ", pprint(msg)
    print "Sentence: ", msg.__class__.__name__

    datestamp = lastDatestamp
    timestamp = lastTimestamp

    # Nx2 doesn't produce date with its logs.
    if hasattr(msg, 'datestamp'):
      datestamp = msg.datestamp
    if hasattr(msg, 'timestamp'):
      timestamp = msg.timestamp

    if datestamp and timestamp:
      print "Last On:  ", datestamp, timestamp
      last_on = datetime.combine(datestamp, timestamp)
      print "Last On:  ", last_on

      ## ------ LAT and LON ------------
      lat = lastLat
      lon = lastLon

      # Only some messages will override
      if hasattr(msg, 'lat') and hasattr(msg, 'lat_dir'):
        lat = (float(msg.lat[:2])+float(msg.lat[2:])/60) * (-1 if msg.lat_dir == 'S' else 1)

      if hasattr(msg, 'lon') and hasattr(msg, 'lon_dir'):
        lon = (float(msg.lon[:3])+float(msg.lon[3:])/60) *(-1 if msg.lon_dir == 'W' else 1)

      print "Last Gps: ", lat, lon 
      point = Point( lat, lon )

      print "Last Point:  "
      pprint(point)

      paramNames = ""
      paramValues = ""

## The dictionary method is awesome
# <WCV(velocity='-7.17', vel_units='N', waypoint_id='046') data=['A']>
      mD = msg.name_to_idx
      for k in mD.keys():
        v = msg.data[mD[k]]

        if not k == "true" and not k == "timestamp":
          if not v.rstrip() == "":
            # does it blend?
            try:
              paramValues += "%f," % float(v)
              paramNames += "%s," % k
            except ValueError:
              paramValues += '"%s",' % v
              paramNames += "%s," % k
     
## The CSV row method is clunky, lets use the NMEA parser to its full power!
#      csv_row = []
#      r = csv.reader([line])
#      for row in r:
#        csv_row = row
#        # Dynmically build the parameter list. , p0s, p0f,  csv_row[1], float(csv_row[1])    
#        for x in range(1, len(csv_row)):
#          paramValues += "'%s'," % csv_row[x]
#          paramNames += "p%ds," % x
#          # does it blend?
#          try:
#            paramValues += "%f," % float(csv_row[x])
#            paramNames += "p%df," % x
#          except ValueError:
#            1 # supress exception


      print "INSERT INTO nmeas ( last_gps_on, last_gps, last_lat, last_lon, nmea_sentence, %s noun, description ) values ( '%s', point(%f,%f), %f, %f, '%s', %s '%s', '%s' );\n" % ( paramNames, last_on, point.latitude, point.longitude, point.latitude, point.longitude, line, paramValues, msg.__class__.__name__, nmeaDict[msg.__class__.__name__] )


      ## Store th values for the next loop
      lastDatestamp = datestamp
      lastTimestamp = timestamp
      lastPoint = point
      lastLat = lat
      lastLon = lon

readf.close()


#
# ^o^
#       |\    ship it!
#       | \   /
#      /|  \
#   __/_|___\_
# ~~\________/~~
#  ~~~~~~~~~~~~

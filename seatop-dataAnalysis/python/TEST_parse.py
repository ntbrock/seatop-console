#!/usr/bin/python


import csv
import pynmea2
from pprint import pprint
from datetime import date, datetime, timedelta
from geopy.point import Point

line1 = "$GPRMC,155954.000,A,3247.2172,N,07954.5710,W,0.00,,140914,,,D*6F"

# taken from nexus
line1 = "$GPGLL,3236.075,N,08010.504,W,130001,A,A*58"

#msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
msg = pynmea2.parse(line1)

print "Message: ", pprint(msg)

print "Sentence: ", msg.__class__.__name__


datestamp = datetime.today
timestamp = msg.timestamp

# Nx2 doesn't produce date with its logs.
if not hasattr(msg, 'datestamp'):
    datestamp = date(2014, 04, 27)
else:
    datestamp = msg.datestamp

last_on = datetime.combine(datestamp, timestamp)

print "Last On:  ", last_on

print "Last Gps: ", msg.lat, msg.lat_dir, "  ", msg.lon, msg.lon_dir

# http://www.experts-exchange.com/Database/GIS_and_GPS/Q_22112629.html
# It is in ddmm.mmmm format for latitude and in dddmm.mmmm for longitude.
# to convert it into dd.dddd fromat you will need to do ddd + mm.mmmm/60
# Geopy Test

last_point = Point( (float(msg.lat[:2])+float(msg.lat[2:])/60) * (-1 if msg.lat_dir == 'S' else 1), (float(msg.lon[:3])+float(msg.lon[3:])/60) *(-1 if msg.lon_dir == 'W' else 1) )

print "Last Point:  "
pprint(last_point)

csv_row = []

r = csv.reader([line1])
for row in r:
  csv_row = row

print "INSERT INTO nmeas ( last_gps_on, last_gps, last_lat, last_lon, noun, sentence, p0s, p0f ) values ( '%s', point(%f,%f), %f, %f, '%s', '%s', '%s', %f);\n" % ( last_on, last_point.latitude, last_point.longitude, last_point.latitude, last_point.longitude, csv_row[0], line1, csv_row[1], float(csv_row[1]) )

# TODO, dynmically build the parameter list.




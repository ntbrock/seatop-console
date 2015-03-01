#!/bin/sh

sleep 15 # wait for usb devices to come online

export BASEDIR=/home/pi/seatop-python

# 2015Mar01 - set the unix time
$BASEDIR/set_unix_time_from_gps.py 0 



echo -n "reboot.sh run at  " 
date


export DATEPART=`date "+%F"`
export DATEDIR="${HOME}/seatop-${DATEPART}"
mkdir -p $DATEDIR


$BASEDIR/cat_nmea_usb.py 0 >> $DATEDIR/nmea_USB0.txt &
$BASEDIR/cat_nmea_usb.py 1 >> $DATEDIR/nmea_USB1.txt & 

#$BASEDIR/cat_nmea_usb.py 2 >> $DATEDIR/nmea_USB2.txt & 
#$BASEDIR/cat_nmea_usb.py 3 >> $DATEDIR/nmea_USB3.txt & 


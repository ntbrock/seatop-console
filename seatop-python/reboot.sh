#!/bin/sh

sleep 15 # wait for usb devices to come online
echo -n "reboot.sh run at  " 
date

export BASEDIR=/home/pi/seatop-python
export DATEDIR=`date "+%F"`
mkdir -p $BASEDIR/$DATEDIR

$BASEDIR/cat_nmea_usb.py 0 >> $BASEDIR/$DATEDIR/nmea_USB0.txt &
$BASEDIR/cat_nmea_usb.py 1 >> $BASEDIR/$DATEDIR/nmea_USB1.txt & 
#$BASEDIR/cat_nmea_usb.py 2 >> $BASEDIR/$DATEDIR/nmea_USB2.txt & 
#$BASEDIR/cat_nmea_usb.py 3 >> $BASEDIR/$DATEDIR/nmea_USB3.txt & 


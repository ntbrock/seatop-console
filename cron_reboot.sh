#!/bin/sh
# 2015-Mar-01 - Have the pi user install this cron to run on boot.

# crontab -e
# @reboot sh /home/pi/seatop-console/reboot.sh >> /home/pi/seatop-console/cronlog 2>&1

#----------------------------------------------------------
# Configure some of the USB ports for your devices.  This could be made more configurable. :)
#  /dev/ttyUSB<n>

export GPS_USB=0
export NX2_USB=1


#----------------------------------------------------------
sleep 20 # wait for usb devices to come online

export BASEDIR=/home/pi/seatop-console/seatop-python

# 2015Mar01 - set the unix time
$BASEDIR/set_unix_time_from_gps.py 0 

echo -n "cron_reboot.sh run at  " 
date

# Build the seatop data directory
export DATEPART=`date "+%F"`
export DATEDIR="${HOME}/seatop-${DATEPART}"
mkdir -p $DATEDIR


### Start the listener

$BASEDIR/cat_nmea_usb.py ${GPS_USB} >> $DATEDIR/nmea_USB${GPS_USB}-gps.txt &
$BASEDIR/cat_nmea_usb.py ${NX2_USB} >> $DATEDIR/nmea_USB${NX2_USB}-nx2.txt & 

#$BASEDIR/cat_nmea_usb.py 2 >> $DATEDIR/nmea_USB2.txt & 
#$BASEDIR/cat_nmea_usb.py 3 >> $DATEDIR/nmea_USB3.txt & 

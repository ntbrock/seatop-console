#!/bin/sh
# 2015-Mar-01 - Every minute, add an alignment timestamp to each process.

# Add to cron:  
# * * * * * /home/pi/seatop-console/cron_1min_timestamp.sh


# 10 = SIGUSR1

kill -10 `cat ${HOME}/gps.pid` `cat ${HOME}/nx2.pid`


seatop-console
==============

Seatop: Unix console application enables NMEA serial monitoring and trending


1. Open serial console via pipe, minicom?

http://logicalgenetics.com/category/software/raspberrypi/

sudo pacman -S minicom

minicom -b 4800 -o -D /dev/ttyAMA0

2. Open sentences into a grid or column

Trend time down, nmea sentences as pages, 
Like a grep.

3. Have a top statistic maybe boat speed or vmg like the system load

4. Design widget layout like the nx2 software

5. Run on raspberry pi with usb serial console to nx2 server

6. Use ANSI art to colorize, Green, red

7. Night mode, red letters using bolds and backgrounds

8. Learn screen to enable paging

9. Raspberry pi becomes wifi AP, boat name

10. Pi has music output, w SD card of mp3

11. Any device can log into pi via ssh, and run seatop by typing s <tab>

12. Post depths to public anonymized server


===

Link to ANSI escape code coloring
http://stackoverflow.com/questions/15682537/ansi-color-specific-rgb-sequence-bash

Night vision red = echo -e "\033[38;5;208mpeach\033[0;00m"


Link to pi MP3 player


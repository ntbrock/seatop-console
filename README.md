seatop-console
==============

Seatop: Unix console application enables NMEA serial monitoring and trending. Developed in Charleston, SC as part of the CORA racing series aboard a J/120.

- Seatop 0.2 - 2015Mar01

Based on raspberry pi, B+ Raspbian 7

Assuming that the GPS (USB type) is /dev/ttyUSB0 and the Nexus server is USB on /dev/ttyUSB1.

The seatop-python scripts will set the system time based on GPS on boot up.

The pi runs as a Wifi access point, 192.168.42.1, and makes the GPS and NX2 NMEA readings available via HTTP for other devices aboard.

Coming soon - Audio output! Tack detector and tunes.

The seatop-dataAnalysis folder is for post-race analysis, including mysql transformation and Tableau workbook samples. Follow the data.

- Seatop Roadmap and Feature List

1. (Done) Run on raspberry pi with usb serial console to nx2 server, capture data to filesystem for shoreside analysis.

2. (Done) Raspberry pi becomes wifi AP, boat name, other devices aboard can connect via ethernet or Wifi.

3. Record and summarize NMEA sentences into a grid or column, posted via http, auto refresh. Viewable via laptop + iPhone wifi devices aboard.

4. Enable pre-race wind tracking stats. Trending, quick visuals.
    Trend time down, nmea sentences as pages, Like a grep.

5. Track speed into and out of tack maneuvers, audio feedback during practices. Gearshifting - 80%, 90%, Full Trim.
  Provice a quick a 'top' statistic maybe boat speed or vmg like the system load over 5 min. Can see easily if we're FASTER over last minute or SLOWER over past 5 minutes, same with wind.

6. Design widget layout like the nx2 software (D3 javasript vis on mobile safari )  For console: Use ANSI art to colorize, Green, red (like htop)

7. Night mode, red letters using bolds and backgrounds

8. Learn screen to enable paging

10. Pi has music output, w SD card of mp3

11. Any device can log into pi via ssh, and run seatop by typing s <tab>

12. Post depths to public anonymized server. Build the open depth database.

===

Link to ANSI escape code coloring
http://stackoverflow.com/questions/15682537/ansi-color-specific-rgb-sequence-bash

Night vision red = echo -e "\033[38;5;208mpeach\033[0;00m"


Link to pi MP3 player


- Seatop 0.1 - 2014, Manual Discovery

Open serial console via pipe, minicom?

http://logicalgenetics.com/category/software/raspberrypi/

sudo pacman -S minicom

minicom -b 4800 -o -D /dev/ttyAMA0


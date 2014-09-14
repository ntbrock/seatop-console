#!/usr/bin/ruby
require 'rubygems'
require 'csv'
require 'fcntl'
require 'curses'
include Curses

# http://home.mira.net/~gnb/gps/nmea.html
NMEA_ROWS = [
             { :subj => "$IIHDM", :desc => "Heading Magnetic" },
             { :subj => "$IIHDT", :desc => "Heading True" },

             { :subj => "$IIDBT", :desc => "Depth Below Transmitter" },
             { :subj => "$IIMWD", :desc => "Wind Direction" },
             { :subj => "$IIVWT", :desc => "True Wind Speed and Angle" },
             { :subj => "$IIVDR", :desc => "Set and Drift" },
             { :subj => "$IIVHW", :desc => "Water Speed and Heading" },

             { :subj => "$IIVTG", :desc => "Track made good and speed over ground" },
             { :subj => "$IIMWV", :desc => "Magnetic Wind Speed and Angle" },

             { :subj => "$GPWCV", :desc => "Waypoint Closure Velocity" },
             { :subj => "$GPXTE", :desc => "Cross Track Error" },
             { :subj => "$GPZDA", :desc => "UTC Date / Time and Local Time Zone Offset" },

             { :subj => "$GPGLL", :desc => "Geographic Position, Latitude/Longitude" },
             { :subj => "$GPGSV", :desc => "GPS Sattelites in View" },

             { :subj => "$IIVPW", :desc => "Speed Measured Parallel to Wind" }
             ]


def rowNumberForSentence(nmeaSubject) 
  0.upto(NMEA_ROWS.length-1) {|rIdx|
    if ( NMEA_ROWS[rIdx][:subj] == nmeaSubject )
      return rIdx
    end
  }
  return 0
end

def metaForSentence(nmeaSubject)
  0.upto(NMEA_ROWS.length-1) {|rIdx|
    if ( NMEA_ROWS[rIdx][:subj] == nmeaSubject )
      return NMEA_ROWS[rIdx]
    end
  }
  return nil
end


#-----------------------------------------------------------



Curses.init_screen

Curses.start_color
# Determines the colors in the 'attron' below
Curses.init_pair(COLOR_BLUE,COLOR_BLUE,COLOR_BLACK) 
Curses.init_pair(COLOR_RED,COLOR_RED,COLOR_BLACK)

begin
  Curses.setpos(0, 0)  # top left
  Curses.addstr("------- SeaTop ALPHA ------------------------------------")
  Curses.refresh

  #

  STDIN.fcntl(Fcntl::F_SETFL,Fcntl::O_NONBLOCK)
  CSV(STDIN) { |csv_in| 
    csv_in.each { |csv_row|

      row = rowNumberForSentence(csv_row[0]) + 1
      nmea = metaForSentence(csv_row[0])

      if nmea != nil then 

        Curses.setpos(row, 0)  # column 6, row 3
        
        Curses.attron(color_pair(COLOR_RED)|A_NORMAL){
          Curses.addstr( nmea[:desc] )
        }
        
        Curses.setpos(row, 25)
        Curses.addstr( csv_row.to_s )
        
        
        Curses.refresh
        
        #col = ( col + 1 ) % max_col
        #row = ( row + 1 ) % max_row
      end

    }
  }
  
 
  Curses.getch  # Wait until user presses some key.
ensure
  Curses.close_screen
end

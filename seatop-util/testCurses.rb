#!/usr/bin/env ruby
require 'rubygems'
require 'curses'
include Curses

Curses.init_screen

Curses.start_color
# Determines the colors in the 'attron' below
Curses.init_pair(COLOR_BLUE,COLOR_BLUE,COLOR_BLACK) 
Curses.init_pair(COLOR_RED,COLOR_RED,COLOR_BLACK)


begin
  Curses.setpos(0, 0)  # top left
  Curses.addstr("------- SeaTop ALPHA ------------------------------------")

  1.upto(60) { |col|
    1.upto(20) { |row|

      Curses.setpos(row, col)  # column 6, row 3

      Curses.attron(color_pair(COLOR_RED)|A_NORMAL){
        Curses.addstr(".")
      }
      
      # Curses.addstr(".")

      #sleep 1
      sleep(1.0/480.0)
      Curses.refresh
    
    }
  }

 
  Curses.getch  # Wait until user presses some key.
ensure
  Curses.close_screen
end

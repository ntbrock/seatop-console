#!/usr/bin/env ruby

# http://rubydoc.info/gems/nmea/0.4/frames

require 'rubygems'
require 'csv'

if ( ARGV.length < 3 ) then
  raise "Usage: readLogFile <rowsPerDelay> <secondDelay> <filename>"
end

rowsPerDelay = ARGV[0].to_i
secondDelay = ARGV[1].to_f
filename = ARGV[2]

fh = File.open(filename, 'r')
rowCount = 1

fh.lines do |line|
  line.chomp!
  print "#{line}\n"

  if ( rowCount % rowsPerDelay == 0 ) then
    sleep secondDelay
  end

  STDOUT.flush

  rowCount += 1
end


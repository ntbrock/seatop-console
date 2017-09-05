#!/usr/bin/env ruby

if ARGV.length < 1 then
  STDERR.puts "Usage: ./toPolarPlot.rb <nmeaFile>"
  raise "Invalid Arguments"
end

nmeaFile = ARGV[0]

line_num=0
text=File.open(nmeaFile).read
text.gsub!(/\r\n?/, "\n")


frame = {}


frames = []

text.each_line do |line|

#  print "#{line_num += 1} #{line}"

  if ( /\$IIVWT/.match(line) ) then
    p = line.split(',')
    # puts "IIVWT: #{p.inspect}"
    frame[:tws] = p[3].to_f.to_i
    frame[:twa] = p[1].to_i
    if p[2] == "L" then
      frame[:twa] = -1 * p[1].to_i
    end

#IIVWT: ["$IIVWT", "106", "R", "09.85", "N", "05.07", "M", "", "*35\n"]
#IIVWT: ["$IIVWT", "104", "R", "09.97", "N", "05.13", "M", "", "*31\n"]
#IIVWT: ["$IIVWT", "103", "R", "09.36", "N", "04.82", "M", "", "*34\n"]

  elsif ( /\$IIVHW/.match(line) ) then
    p = line.split(',')
    # puts "IIVHF: #{p.inspect}"

#IIVHF: ["$IIVHW", "271", "T", "278", "M", "06.65", "N", "12.31", "K*58\n"]
#IIVHF: ["$IIVHW", "271", "T", "278", "M", "06.54", "N", "12.11", "K*58\n"]
#IIVHF: ["$IIVHW", "271", "T", "278", "M", "06.49", "N", "12.01", "K*55\n"]

    frame[:hdm] = p[3].to_f.to_i
    frame[:bsp] = p[5].to_f

    if frame[:bsp] > 1 && frame[:tws] > 8 && frame[:tws] < 13 then
      frames.push(frame)
    end
    frame = {}

  end
# $IIVWT,031,R,12.79,N,06.58,M,,*30

end

byTws = []
0.upto(30) do |tws|
  #puts "tws: #{tws}"

  # find matching tws

  matchingFrames = []
  frames.each do |frame|

    if ( frame[:tws] == tws ) then

      matchingFrames.push(frame)
    end
  end
  

  byTws[tws] = matchingFrames
end


puts "var twa = ["
# build twa array
0.upto(30) do |tws|
  puts "["
  byTws[tws].each{|frame|
    print "#{frame[:twa]},"
  }
  puts "],\n"
end
puts "]"

puts "var bsp = ["
# build bsp array
0.upto(30) do |tws|
  puts "["
  byTws[tws].each{|frame|
    print "#{frame[:bsp]},"
  }
  puts "],\n"
end
puts "]"



#puts "frames:"
#puts frames.inspect


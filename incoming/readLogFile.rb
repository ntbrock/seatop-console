#!/usr/bin/env ruby

# http://rubydoc.info/gems/nmea/0.4/frames

require 'rubygems'
require 'csv'

if ( ARGV.length < 1 ) then
  raise "Usage: readLogFile <logFile>"
end

@sent_idx = 1
@sent = {}

CSV.foreach(ARGV[0]) do |line|
  # puts "CSV #{line.inspect}"

  @sent[line[0]] ||= {}

  if ( ! @sent[line[0]][:index] ) then
    @sent[line[0]][:index] = @sent_idx
    @sent_idx += 1
  end

  @sent[line[0]][:lines] ||= []
  @sent[line[0]][:lines] << line

end

drawSent()

def drawSent
  @sent.keys.each do |k|
    print "key: #{k}  count: #{sent[k][:lines].size}  index: #{sent[k][:index]}\n"
  end
end

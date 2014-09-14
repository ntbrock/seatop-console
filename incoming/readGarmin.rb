#!/usr/bin/env ruby

# http://rubydoc.info/gems/nmea/0.4/frames

require 'rubygems'
gem 'serialport'
gem 'nmea'

@sp = SerialPort.open("/dev/tty.usbserial", 4800, 8, 1, SerialPort::NONE)
@handler = NMEAHandler.new

while(@sentence = @sp.gets) do
  NMEA.scan(@sentence, @handler)
end

#!/usr/bin/env ruby

require 'rubygems'
require 'httpclient'

http = HTTPClient.new
resp = http.get "http://jonx.org/ip.php"

print "#{resp.body}\n"


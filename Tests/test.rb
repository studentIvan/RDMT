require 'socket'
include Socket::Constants

s = Socket.new AF_INET, SOCK_STREAM
s.connect Socket.pack_sockaddr_in(3308, '127.0.0.1')
s.puts 'test:2'
puts s.gets
s.close
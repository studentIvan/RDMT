import socket

# without API, only work mechanism =(

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 3308))

s.send('test:2')
data = s.recv(1);
if data == '1':
	print "1 - accept"
else:
	print "1 - not accept"
	
s.send('test:2')
data = s.recv(1);
if data == '1':
	print "2 - accept"
else:
	print "2 - not accept"
	
s.send('test:2')
data = s.recv(1);
if data == '1':
	print "3 - accept"
else:
	print "3 - not accept"

s.close()
#!/bin/python3
import sys # allow us to enter command line arguement
import socket # connect the port and connections
from datetime import datetime

#Define target
#python3 Portcanner.py <ip>
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])# translate host name to IPv4
else:
	print("Invalid amount of arguement")
	print("Syntax python3 Portcanner.py <ip>")
	sys.exit()

#Add a pretty banner
print("-" * 50)
print("Scanning target"+target)
print("Time started" + str(datetime.now()))# Time stamp
print("-" * 50)

try:
	for port in range(0,65000):
		s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)# connection variable
		socket.setdefaulttimeout(1)# is a float 
		result = s.connect_ex((target,port))# returns error indicator
		if result ==0:
			print("Port {} is open".format(port))
			s.close()
except KeyboardInterrupt:
	print("\n Exiting programing")
	sys.exit()
except socket.gaierror():
	print("Hostname cannot be resolved")
	sys.exit()
except socket.error:
	print("Coudnot connect")
	sys.exit()


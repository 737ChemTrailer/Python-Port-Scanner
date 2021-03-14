#!/bin/python3

import sys
import socket
from datetime import datetime

#Define the target
#Translate a hostname to IPv4 if required
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add banner
print("-" * 50)
print("Scanning target: ", target)
print("Time started: ", str(datetime.now()))
print("-" * 50)

#Set the port range of your chocie (0, 65535) in the for loop
#Set a 1 sec pause at port if it is open
#If return is 0, port is open, 1 means it is closed
try:
	for port in range(50,450):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port #: ", port, " is open")
		s.close()
#Set up clean exit scenarios
#keyboard interrupt
#DNS fail to resolve hostname
#Failure to make a connection to the IP address - socket error
except KeyboardInterrupt:
	print("\nExiting Scan.")
	sys.exit()
	
except socket.gaierror:
	print("Error: Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Error: Couldn't connect to server.")
	sys.exit()


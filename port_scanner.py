#!/bin/python3

import sys
import socket
from datetime import datetime

	
#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 port_scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("_" * 50)

port_start = int(input("what is the starting port? "))
port_end = int(input("What is the ending port? "))
port_end += 1


try:
	for port in range(port_start, port_end):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()

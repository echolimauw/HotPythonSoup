#!/usr/bin/python

import os
import re
import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) > 3:
	print("No more than two arguments, please.")

def argCheck():
	try:
		ipStr = sys.argv[1]
		

def ping_this_IPv4(ip):
	try:
		subprocess.run(["ping ", "-c ", "4 ", ip], check=True)
		return True
	return False

def is_port(portStr):
	if re.match(r'^\d{1,5}$', portStr):
		portNum = int(portStr)
		if portNum <= 65535:
			return True
	return False

def is_valid_IPv4(ipStr):
	if re.match(r'^(\d{1,3}\.){3}\d{1,3}$'):
		return bool(ping_this_IPv4(ipStr))


def portscanner(host, port):
	if sock.connect_ex((host,port)):
		print(f"Port {port} is closed")
	else:
		print(f"Port {port} is open")

def main ():




if __name__ == "__main__"
	main()

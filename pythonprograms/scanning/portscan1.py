#!/usr/bin/python

import os
import re
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipStr = input("Please enter host ip to scan: ")
portStr = input("Please enter port number to scan: ")


if len(sys.argv) > 3:
	print("No more than two arguments, please.")

def is_port(portStr):
	if re.match(r'^\d{1,5}$', portStr):
		portNum = int(portStr)
		if portNum <= 65535:
			return True
	return False

def is_valid_IPv4(ipStr):
	if re.match(r'^(\d{1,3}\.){3}\d{1,3}$'):
		return True
	else:
		return False

def portscanner(host, port):
	if sock.connect_ex((host,port)):
		print(f"Port {port} is closed")
	else:
		print(f"Port {port} is open")

def main():

	if is_valid_IPv4(ipStr):
		ipStr = host
	else:
		print("Please try again with a valid IPv4 address."

	if is_port(portStr):
		portStr = port
	else:
		print("Please try again with a valid port number."

	portscanner()

if __name__ == "__main__"
	main()

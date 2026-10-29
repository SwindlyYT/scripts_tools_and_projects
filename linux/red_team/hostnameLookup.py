#!/usr/bin/env python3

import os
import subprocess
import ipaddress

def run(args):

	#parameters
	output_file = "/home/kali/hostnameLookup.txt"
	ip_address = "192.168.1.0/24"

	if len(args) > 2:

		for i in range(1, len(args)):
			i = args[i].split("=")
			
			if i[0] == "output_file":
				output_file = i[1]
			
			elif i[0] == "ip_address":
				ip_address = i[1]
				
			elif i[0] == "-h" or i[0] == "-help":
				print("output_file=[file]\t\tThis can be absolute or relative path. Default is /home/kali/hostnameLookup.txt\n")
				print("ip_address=[ip network]\t\tThis is the IP address with dot notation for the network you wish to scan. Default is 192.168.1.0/24\n")
				print("-h or -help\t\tThis brings up the help page")
				
				return

	try:
		network = ipaddress.ip_network(ip_address)
	except ValueError: 
		print("Invalid IP address or CIDR notation. Possible slash notation is /1-/30")
		return
	

	os.system(f"echo  > {output_file}")

	for ip in network.hosts():
		output = subprocess.run(f"nslookup {ip}", shell = True, capture_output=True)
		output = output.stdout.decode("utf-8")
		output = output.strip("\n")
		if not output.endswith("NXDOMAIN"):
			os.system(f"echo {output} >> {output_file}")


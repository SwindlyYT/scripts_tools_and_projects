#!/usr/bin/env python3

import os
import subprocess
import ipaddress


def run(args)
	
	output_file = "/home/kali/portScan.txt"
	input_file = ""
	reverse = False
	
	if len(args) > 2:

		for i in range(1, len(args)):
			i = args[i].split("=")
			
			if i[0] == "output_file":
				output_file = i[1]
			
			elif i[0] == "input_file":
				input_file = i[1]
				
			elif i[0] == "-reverse":
				reverse = True
				
			elif i[0] == "-h" or i[0] == "-help":
				print("output_file=[file]\t\tThis can be absolute or relative path. FILE WILL BE CLEARED ON RUN. Default is /home/kali/portScan.txt\n")
				print("input_file=[file]\t\tThis HAS to be absolute path unless you are in that location. IP addresses need to be 1 per line and if they are reverse then use the -reverse parameter\n")
				print("-reverse\t\tThis shows that the file has the IP address in reverse order. Default is False\n")
				print("-h or -help\t\tThis brings up the help page for this script\n")
				
				return
	
	if input_file == "":
		print("An input file IS required")
	
		return
		
	if reverse:
		with open(input_file, "r") as file:
			for line in file:
				line = line.split(".")
				ip = [line[3], line[2], line[1], line[0]]
				
				output = subprocess.run(f"nmap -Pn -sS {ip}", shell = True, capture_output=True)
				os.system(f"echo {output} >> {output_file}")
				os.system("echo \n\n\n\n >> {output_file}")
				
	else:
		with open(input_file, "r") as file:
			for line in file:
				ip = line.strip("\n")
				ip = ip.strip(" ")
				output = subprocess.run(f"nmap -Pn -sS {ip}", shell = True, capture_output=True)
				os.system(f"echo {output} >> {output_file}")
				os.system("echo \n\n\n\n >> {output_file}")
				
			

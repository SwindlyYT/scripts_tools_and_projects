#!/usr/bin/env python3

import sys

import hostnameLookup
import portScan

args = sys.argv

count = len(args)

def main():
	if len(args) > 1:
		
		if args[1] == "hostnameLookup":
			hostnameLookup.run(args)
			
		elif args[1] == "portScan":
			portScan.run(args)
		
		elif args[1] == "-h" or args[1] == "-help":
			print("hostnameLookup [parameter] [parameter] etc.\t\tDefault it will use the defaults. Add -h for the help section of that script\n")
			print("portScan [parameter] [parameter] etc.\t\tDefault it will use the defaults. Add -h for the help section of that script\n")
			print("-h or -help\t\tBrings up the help page for all parameters of the main script. Basically just all the script names\n")
			
			return
		
	else:
		print("No parameters set. Please use -h or -help to get a list of scripts") 
		
		return

main()
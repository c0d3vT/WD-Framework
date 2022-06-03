#!/usr/bin/env python3
import os
import time
from colorama import *

# Banner  
def banner():
	print(Fore.GREEN)
	print("""
	'##:::::'##:'########::'########:'##::::'##:'####:'##::::::::'######::
	 ##:'##: ##: ##.... ##: ##.....:: ##:::: ##:. ##:: ##:::::::'##... ##:
	 ##: ##: ##: ##:::: ##: ##::::::: ##:::: ##:: ##:: ##::::::: ##:::..::
	 ##: ##: ##: ##:::: ##: ######::: ##:::: ##:: ##:: ##:::::::. ######::
	 ##: ##: ##: ##:::: ##: ##...::::. ##:: ##::: ##:: ##::::::::..... ##:
	 ##: ##: ##: ##:::: ##: ##::::::::. ## ##:::: ##:: ##:::::::'##::: ##:
	. ###. ###:: ########:: ########:::. ###::::'####: ########:. ######::
	:...::...:::........:::........:::::...:::::....::........:::......:::
	""")

# Menu
def revgene():
	print("""
	-------------------------------------
	  1 - Python
	  2 - Bash
	  3 - PHP
	  4 - Javascript
	  5 - Powershell
	  6 - NetCat
	  7 - APK
	  8 - EXE
	-------------------------------------
	""")
	revgentype = input("[#] Select a type of shell ===> ")
	if revgentype == "1":
		print(Fore.GREEN, "[+] Generating a Python Reverse Shell .....")
		os.system("bash revgen/pythongen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "2":

		print(Fore.GREEN, "[+] Generating a BASH Reverse Shell .....")
		os.system("bash revgen/bashgen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "3":

		print(Fore.GREEN, "[+] Generating a PHP Reverse Shell .....")
		print("[!] Note Modify The File And But Your LHOST LPORT Manully ...")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "4":

		print(Fore.GREEN, "[+] Generating a Javascript Reverse Shell .....")
		os.system("bash revgen/javascriptgen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "5":

		print(Fore.GREEN, "[+] Generating a Powershell Reverse Shell .....")
		os.system("bash revgen/powershellgen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "6":

		print(Fore.GREEN, "[+] Generating a NetCat Reverse Shell .....")
		os.system("bash revgen/netcatgen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "7":

		print(Fore.GREEN, "[+] Generating a APK Reverse Shell .....")
		os.system("bash revgen/apkgen.sh")
		print("[+] Done file stored in ../wd-generated .")
	elif revgentype == "8":

		print(Fore.GREEN, "[+] Generating a BASH Reverse Shell .....")
		os.system("bash revgen/exegen.sh")
		print("[+] Done file stored in ../wd-generated .")
#################################################################################################
def menu():
	banner()
	print(Fore.CYAN)
	print("""
-----------------------------------------------------------------------
1 - Reverse Shell Generators
2 - Network Scanner
3 - Packet Sniffer
4 - ARP Spoofer
5 - Tools Installers
------------------------------------------------------------------------
""")
	while True:
		command = input("[#] Enter a number ==> ")
		if command == "exit":
			break
		elif command == "1":
			revgene()
		elif command == "2":
			os.system("sudo python3 tools/NetworkScanner.py")
		elif command == "3":
			print(Fore.CYAN, "Packet Sniffer By : EONRaider")
			os.system("sudo ./tools/packet_sniffer")
		elif command == "4":
			print("sudo bash tools/ARPSpoof.sh")
		elif command == "4":
			os.system("sudo python3 tools/Installer.py")
	
menu()
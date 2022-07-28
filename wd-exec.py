#!/usr/bin/env python3

# Import the required libs

import os
import click 
from colorama import *
import webbrowser as webr

# Checking if user is root

if os.geteuid() != 0:
	print(Fore.RED)
	exit("[!]==[  Please run the script as root ]==[!]\n")


print(Fore.CYAN)


# Define a function to generate a banner

def show_banner():
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
# add the commands group
@click.group()
def cli():
	pass
@cli.command()
# set the reverse generator function
def rev():
	print(Fore.CYAN)
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
	revgentype = input("[+]===[ Type ]==> ")
	if revgentype == "1":
		print(Fore.GREEN, "[+] Generating a Python Reverse Shell .....")
		os.system("bash /opt/WD-Framework/tools/revgen/pythongen.sh")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "2":

		print(Fore.GREEN, "[+] Generating a BASH Reverse Shell .....")
		os.system("bash /opt/WD-Framework/revgen/bashgen.sh")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "3":

		print(Fore.GREEN, "[+] Generating a PHP Reverse Shell .....")
		print("[!] Note Modify The File And But Your LHOST LPORT Manully ...")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "4":

		print(Fore.GREEN, "[+] Generating a Javascript Reverse Shell .....")
		os.system("bash /opt/WD-Framework/revgen/javascriptgen.sh")
		print("[+] Done file stored in ../wd-generated .")


	elif revgentype == "5":

		print(Fore.GREEN, "[+] Generating a Powershell Reverse Shell .....")
		os.system("bash /opt/WD-Framework/powershellgen.sh")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "6":

		print(Fore.GREEN, "[+] Generating a NetCat Reverse Shell .....")
		os.system("bash /opt/WD-Framework/revgen/netcatgen.sh")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "7":

		print(Fore.GREEN, "[+] Generating a APK Reverse Shell .....")
		os.system("bash /opt/revgen/apkgen.sh")
		print("[+] Done file stored in /opt/wd-generated .")


	elif revgentype == "8":

		print(Fore.GREEN, "[+] Generating a BASH Reverse Shell .....")
		os.system("bash /opt/WD-Framework/revgen/exegen.sh")
		print("[+] Done file stored in /opt/wd-generated .")

# set the nets network scanner command
@cli.command()
def nets():
	os.system("sudo python3 /opt/WD-Framework/tools/NetworkScanner.py")

# set the sniffer command

@cli.command()
def sniff():
	os.system("sudo python3 /opt/WD-Framework/tools/packet_sniffer/sniffer.py")

# set the arpspoof command
@cli.command()
def spoof():
	os.system("sudo bash /opt/WD-Framework/tools/ARPSpoof.sh")


# set a command to print the banner 
@cli.command()
def banner():
	show_banner()


# Run an Html File in the browser
@cli.command()
def webpage():
	os.system("cd /opt/WD-Framework/webapp/ && python3 -m http.server")
	webr.open("localhost:8000")

# Run the essinteial tools installer
@cli.command()
def installer():
	os.system("sudo bash /opt/WD-Framework/tools/essiential-installer.sh")


if __name__ == '__main__':
	cli()

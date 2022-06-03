#!/usr/bin/env python3
import os
from colorama import *

def menu():
	print(Fore.RED, "----------------------------------------------")
	print(Fore.CYAN, "\t [ Installer WD-Team ]")
	print(Fore.RED, "----------------------------------------------")
	print(Fore.RED, """
		1 - Kali linux
		2 - Debian or Debian Based
		3 - Arch or Arch Based 
		""")
	os_type = input("[#] Enter Your OS : ")
	if os_type == 
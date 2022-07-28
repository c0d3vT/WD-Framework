#!/usr/bin/env python3
import os
import platform
import socket
import time
import threading
from queue import Queue
from datetime import datetime
from colorama import *

################################### | Ping Sweep | ###################################
def pingsweep():
	print(Fore.CYAN)
	net = input("[#]==[IP address]==:> ")
	net1 = net.split('.')
	a = '.'

	net2 = net1[0] + a + net1[1] + a + net1[2] + a
	st1 = int(input("[#]Enter the Starting Number: "))
	en1 = int(input("[#]Enter the Last Number: "))
	en1 = en1 + 1
	t1 = datetime.now()

	def scan(addr):
	   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	   socket.setdefaulttimeout(1)
	   result = s.connect_ex((addr,135))
	   if result == 0:
	      return 1
	   else :
	      return 0

	def run1():
	   for ip in range(st1,en1):
	      addr = net2 + str(ip)
	      if (scan(addr)):
	      	print(Fore.GREEN)
	      	print (addr , " : Is Live")
	      	print(Fore.CYAN)
	run1()
	t2 = datetime.now()
	total = t2 - t1
	print ("[+]==[Scanning completed in]==:> " , total)

################################### | Port Scanner | ###################################
def portscanner():
	socket.setdefaulttimeout(3)
	print_lock = threading.Lock()
	print(Fore.CYAN)
	target = input('[#]==[Host Name]==:> ')
	t_IP = socket.gethostbyname(target)
	print ('[+] Starting Scan On Host: ', t_IP)

	def portscan(port):
	   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	   try:
	   	con = s.connect((t_IP, port))
	   	with print_lock:
	   		print(port, ' : Is Open')
	   	con.close()
	   except:
	   	pass
	def threader():
		while True:
			worker = q.get()
			portscan(worker)
			q.task_done()
	      
	q = Queue()
	startTime = time.time()
	   
	for x in range(100):
		t = threading.Thread(target = threader)
		t.daemon = True
		t.start()
	   
	for worker in range(1, 500):
		q.put(worker)
	   
	q.join()
	print(Fore.GREEN)
	print('[+] Time taken:', time.time() - startTime)

################################### | Menu | ###################################
def menu():
	print(Fore.CYAN)
	print("""
------------------------------------------------
\t | Network Scanner WD-Team |
------------------------------------------------
	1 - Port Scanner 
	2 - Ping Sweep
	3 - Exit
------------------------------------------------
		""")
	nettype = input("[#]==[Enter Number]==:> ")
	if nettype == "1":
		portscanner()
	elif nettype == "2":
		pingsweep()

	elif nettype == "exit":
		exit()
	else:
		print(Fore.RED)
		print("[!]==[ ERROR ]==:> Unkown Command [ " + nettype + " ]")
		menu()
menu()

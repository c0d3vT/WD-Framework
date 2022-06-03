#!/usr/bin/env bash
clear
echo "[+] Start Installing ..........."

sudo apt update
sudo apt install python3 python3-pip python3-wheel python3-setuptools gcc g++ chromium-browser hydra wireshark tshark mdk4 nmap ettercap-graphical xterm hcxdumptool hcxtools cmake make hashcat -y
sudo apt install perl curl wget postgresql ruby gems bundler macchanger wine build-essential openjdk-17-jre -y
sudo apt install nikto recon-ng smbmap sqlmap john dsniff netsniff-ng aircrack-ng backdoor-factory weevely  wifite crunch cupp netdiscover openvpn dnsutils net-tools -y
sudo apt install procps iproute2 gawk pciutils telegram-desktop hostapd kdenlive krita lighttpd iptables isc-dhcp-server  dnsmasq reaver bully pixiewps openssl -y
wget "https://download.sublimetext.com/sublime-text_build-4126_amd64.deb" -O sublime_text.deb && sudo apt install ./sublime_text.deb
wget "https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.3.0.deb" -O maltego.deb && sudo apt install maltego.deb
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
#git clone 'https://github.com/beefproject/beef.git'
#sudo ./beef/msfinstall				
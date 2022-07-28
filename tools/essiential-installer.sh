#!/usr/bin/env bash
clear

echo " "
echo "[+]========[ Start Installing ]========[+]"
echo " "

sudo apt update

sudo apt install perl curl wget postgresql ruby gems bundler macchanger build-essential python3 python3-pip python3-wheel python3-setuptools gcc g++ hydra wireshark tshark mdk4 nmap ettercap-graphical xterm hcxdumptool hcxtools cmake make hashcat -y

sudo apt install procps iproute2 gawk pciutils hostapd lighttpd iptables isc-dhcp-server  dnsmasq reaver bully pixiewps openssl nikto recon-ng smbmap sqlmap john dsniff ndiff ncat hydra-gtk netsniff-ng aircrack-ng backdoor-factory weevely  wifite crunch cupp netdiscover openvpn dnsutils net-tools -y

# Install Metasploit-Framework

curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \

  chmod 755 msfinstall && \

  ./msfinstall

# Install Empire

git clone --recursive https://github.com/BC-SECURITY/Empire.git
sudo ./Empire/setup/install.sh

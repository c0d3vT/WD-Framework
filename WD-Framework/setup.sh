#!/usr/bin/env bash
sudo mkdir /opt/wd-generated/
sudo mkdir /opt/WD-Framework
cp -r * /opt/WD-Framework/
echo "--------------------------------------"
echo "	[WD-Framework] Setup ..........."
echo "--------------------------------------"

echo "[+] Setup has been started ...."
sudo apt update 
sudo chmod +x *
sudo python3 -m pip install requirements.txt
sudo ln /opt/WD-Framework/wd-run.py /usr/bin/

read -p "Do you want to install some hacking tools (y/n) : " usr_ins

if [[ $usr_ins == "y" || $usr_ins == "Y" || $usr_ins == "yes" ||  $usr_ins == "Yes" ]]; then
 	sudo bash /opt/WD-Framework/tools/essiential-installer.sh
 else 
 	echo "[+] All set !!!"
 fi 
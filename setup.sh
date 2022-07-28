#!/usr/bin/env bash

# Check Root Privlages
if [ "$EUID" -ne 0 ]
  then echo "[!]==[ Please Run The Script As Root ]==[!]"
  exit
fi

echo "[+]===[ Setup Has Been Started ]===[+]"
python3 -m pip install requirements.txt`
# make dirctory for the generated reverse shells 
sudo mkdir /opt/wd-generated/

# make dirctory for the program it self
sudo mkdir /opt/WD-Framework

# copying the files to the right path
cp -r * /opt/WD-Framework/

# simple banner
echo "--------------------------------------"
echo "[!]========[WD-Framework]==========[!]"
echo "--------------------------------------"

sudo chmod +x *
sudo echo "#!/bin/bash" >> /usr/bin/wdf_exec
sudo mv /opt/WD-Framework/tools/wdf.sh >> /usr/bin/wdf 
sudo chmod +x /usr/bin/wdf
#sudo ln /opt/WD-Framework/wd-exec.py /usr/bin/

read -p "[?]===[ Install Hacking Tools ]===[Y/n]:> " usr_ins

if [[ $usr_ins == "y" || $usr_ins == "Y" || $usr_ins == "yes" ||  $usr_ins == "Yes" || $usr_ins == "" ]];
  then sudo bash /opt/WD-Framework/tools/essiential-installer.sh
    echo "[+] All set !!!"
 else 
 	echo "[+] All set !!!"
 fi 

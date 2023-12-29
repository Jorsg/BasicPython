# noinspection PyUnresolvedReferences
import socket

from socket import *

if __name__ == '__main__':
   equipo  = input('Ingresar la ip del equipo:  ')
   ipequipo = gethostbyname(equipo)
   print('Comenzando a scanear la ip', ipequipo);
   
   for puerto in range(19, 1000):
    cliente = socket(AF_INET, SOCK_STREAM)
    resultado = cliente.connect_ex((ipequipo, puerto))
    if (resultado == 0):
      print('Puerto %d: Abierto'  %(puerto));
      cliente.close()
   
 #print("No ingresa")  

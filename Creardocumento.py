#!/usr/bin/python

documento = open("G:\Practica Python\prueba.txt","r")

for linea in documento.readlines():
    print(linea.strip())
    
documento.close()    
    
    
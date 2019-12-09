#PROGRAMA 30
#Ejercicio 30 condicional multiple
import os
clientes=0
#INPUT VIA OS
clientes=int(os.sys.argv[1])
#Processing
#si la tienda vende 1500 juguetes
#declarar "ventas insuficientes"
if  (clientes<1500):
    print("ventas insuficientes")
if  (clientes>1500)and(clientes<1800):
    print("ventas regulares")
#finif

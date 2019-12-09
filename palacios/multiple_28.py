#PROGRAMA 28
#Ejercicio 28 condicional multiple
import os
dias=0
#INPUT VIA OS
dias=int(os.sys.argv[1])
#processing
#Si el producto supera los 22 dias
#aplicar descuento
descuento=dias>22
if(dias>22):
    print("descuento 50%")
if(dias<22)and(dias>15):
    print("descuento 30%")
#finif

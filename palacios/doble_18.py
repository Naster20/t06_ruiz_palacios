#PROGRAMA 18
#Ejercicio 18 condicional doble
import os
dias=0
#INPUT VIA OS
dias=int(os.sys.argv[1])
#processing
#Si el producto supera los 22 dias
#aplicar descuento
descuento=dias>22
if(dias>22):
    print("con descuento")
else:
    print("sin descuento")
#finif

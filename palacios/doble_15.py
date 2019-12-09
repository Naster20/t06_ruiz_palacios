#PROGRAMA 15
#Ejercicio 15 condicional doble
import os
ejercicio=0
#INPUT VIA OS
ejercicio=int(os.sys.argv[1])
#processing
#Si el numero no supera 200
#mostrar "Desaprobado"
desaprobado=ejercicio<200
if(ejercicio<200):
    print("Desaprobado")
else:
    print("Aprobado")
#finif

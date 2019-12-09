#PROGRAMA 25
#Ejercicio 25 condicional multiple
import os
ejercicio=0
#INPUT VIA OS
ejercicio=int(os.sys.argv[1])
#processing
#Si el numero no supera 200
#mostrar "Desaprobado"
desaprobado=ejercicio<200
if  (ejercicio<200):
    print("Desaprobado")
if  (ejercicio>190)and(ejercicio<199):
    print("pero tiene chance de dar prueba de recuperacion")
#finif

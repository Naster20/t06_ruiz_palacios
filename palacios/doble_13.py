#PROGRAMA 13
#Ejercicio 13 condicional doble
import os
peso_bajado,peso1,peso2=0.0,0.0,0.0
#INPUT VIA OS
peso1=int(os.sys.argv[1])
peso2=int(os.sys.argv[2])
#Processing
#si bajo 7 kg mostrar
#excelente comentario
peso_bajado=peso1-peso2
if(peso_bajado>7):
    print ("EXCELENTE ENTRENAMIENTO")
else:
    print("MAL ENTRENAMIENTO")
#fin_if

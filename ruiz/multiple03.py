# Programa 03
#Tipo de alumno
import os
#Declaracion de variables
alumno=""
nota1=0.0
nota2=0.0
nota3=0.0
prom=0.0
mensaje=""
#INPUT VIA OS
alumno=(os.sys.argv[1])
nota1=float(os.sys.argv[2])
nota2=float(os.sys.argv[3])
nota3=float(os.sys.argv[4])
#PROCESSING
prom=float((nota1+nota2+nota3)/3)
#Si el promedio del alumno es >= a 15 sera bueno
if  (prom < 11):
    mensaje="malo"
#Si es menor sera considerado "Regular"
elif (prom >= 11 ) and (prom <= 15):
    mensaje = "Regular"
elif (prom > 15) and (prom <= 17):
    mensaje = "Bueno"
elif (prom > 17) and (prom <= 20):
    mensaje = "Excelente"
else:
    mensaje = "Revise datos"
print(prom,mensaje)
#fin_if

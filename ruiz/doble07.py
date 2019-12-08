#Programa 07
import os
#Declaracion de variables
alumno=""
nota=0.0
mensaje=""
#Input via OS
alumno=(os.sys.argv[1])
nota=float((os.sys.argv[2]))
#Processing
if(nota >= 11):
    mensaje=("(APROBADO)")
else:
    mensaje=("(DESAPROBADO)")
#Output
print(alumno,"Tu condicion es : ",mensaje)
#fin_if

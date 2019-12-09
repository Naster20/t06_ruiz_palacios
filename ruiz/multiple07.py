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
if(nota >= 11) and (nota <= 14):
    mensaje=("(Pasa a sustitutorio)")
elif(nota > 14) and (nota <= 20):
    mensaje=("(Aprobado)")
else:
    mensaje=("(Desaprobado)")
#Output
print(alumno,"Tu condicion es : ",mensaje)
#fin_if

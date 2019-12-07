# Programa 04
import os
#DECLARACION DE VARIABLES
alumno=""
edad=0
mensaje=""

#INPUT VIA OS
alumno=os.sys.argv[1]
edad=int((os.sys.argv[2]))
#PROCESSING
#Si su edad es superior a los 18 años sera considerado mayor de edad
if(edad >= 18):
    mensaje= "mayor de edad"

#OUTPUT
print(alumno,"su edad es :",edad,"(",mensaje,")")

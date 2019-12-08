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
    mensaje= "Mayor de edad"
#Si su edad es inferior a los 18 años sera considerado menor de edad
else:
    mensaje="Menor de edad"
#OUTPUT
print(alumno,"su edad es :",edad,"Años""(",mensaje,")")
#fin_if

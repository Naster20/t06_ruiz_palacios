# Programa 04
import os
#DECLARACION DE VARIABLES
usuario=""
edad=0
mensaje=""
#INPUT VIA OS
usuario=os.sys.argv[1]
edad=int((os.sys.argv[2]))
#PROCESSING
#Si su edad es superior a los 18 años sera considerado mayor de edad
if(edad > 0) and (edad < 6 ):
    mensaje= "Infancia"
elif(edad > 6) and (edad < 12 ):
    mensaje= "Niñez"
elif(edad > 12) and (edad < 18 ):
    mensaje= "Adolescente"
elif(edad > 18) and (edad < 26 ):
    mensaje= "Adultez"
elif(edad > 26) and (edad < 60 ):
    mensaje= "Segunda Adultez"
else:
    mensaje="Anciano"
#OUTPUT
print(usuario,"su edad es :",edad,"Años""(",mensaje,")")
#fin_if

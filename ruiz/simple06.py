#Programa 06
import os
#Declaracion de variables
empleado=""
categoria=""
mensaje=""
#Input via OS
empleado=os.sys.argv[1]
categoria=os.sys.argv[2]
#processing
#si el tipo de empleado es "nombrado"
#y su categoria es "cas" moestrar "Pertenece a planilla"
#pertenece a planilla = ( aux = tc )
if(empleado == "nombrado") and (categoria == "cas"):
     mensaje= "Pertenece a planilla"
#output
print(mensaje)
#fin_if

#Programa 06
import os
#Declaracion de variables
empleado=""
categoria=""
mensaje=""
#Input via OS
empleado=os.sys.argv[1]
categoria=os.sys.argv[2]
#Processing
#Si el tipo de empleado es "nombrado"
#Si su categoria es "cas" mostrar "Pertenece a planilla"
if(empleado == "nombrado") and (categoria == "cas"):
     mensaje= "Pertenece a Planilla"
#Si no es "nombrado" y tampoco pertence a la categoria "cas"
#mostrar "No Pertenece a Planilla"
else:
    mensaje = "No Pertenece a Planilla"
#Output
print(mensaje)
#fin_if

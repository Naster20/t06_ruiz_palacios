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
#Si el tipo de empleado es "Nombrado"
#Si su categoria es "Cas" mostrar "Pertenece a planilla"
if(empleado == "Nombrado") and (categoria == "Cas"):
     mensaje= "Pertenece a Planilla"
#Si el tipo de empleado es "Nombrado"
#Si su categoria es "Aux" mostrar "Se le agregara a planilla el mes que viene"
elif(empleado == "Nombrado") and (categoria == "Aux"):
     mensaje= "Se le agregara a planilla el mes que viene"
#Si no es "Nombrado" y tampoco pertence a la categoria "Cas"
#mostrar "No Pertenece a Planilla"
else:
    mensaje = "Revise los datos"
#Output
print(mensaje)
#fin_if

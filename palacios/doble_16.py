#PROGRAMA 16
#Ejercicio 16 condicional doble
import os
tipo_de_empleado=""
categoria=""
#INPUT VIA OS
tipo_de_empleado=os.sys.argv[1]
categoria=os.sys.argv[2]
#processing
#si el tipo de empleado es "aux"
#y su categoria es "tc" moestrar "regular"
#regula=(aux=tc)
if(tipo_de_empleado == "aux") and (categoria == "tc"):
    print("regular")
else:
    print("irregular")
#finif

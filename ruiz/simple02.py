# Programa 02
#Area de un rectangulo
import os
#Declaracion de variables
base=0.0
altura=0.0
area=0.0

#INPUT VIA OS
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#PROCESSING

area=(base*altura)

#OUTPUT
print("El area del rectangulo es :",area)

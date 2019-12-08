# Programa 02
#Area de un rectangulo
import os
#Declaracion de variables
base=0.0
altura=0.0
area=0.0
mensaje=""
#INPUT VIA OS
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
#PROCESSING
area=(base*altura)
#Si el area supera los 50 mts^2 se considerara "Area Grande"
if(area > 100):
    mensaje = "Area Grande"
# Si el area es menor a 50 mts^2 se considerara "Area Pequeña"
else:
    mensaje = "Area Pequeña"
#OUTPUT
print("El area del rectangulo es :",area,"mts^2",mensaje)
#fin_if

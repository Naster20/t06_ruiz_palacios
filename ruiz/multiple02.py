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
#Si el area es = 0 0 <= 200 se considerara "Area Pequeña"
if(area == 0) or (area <= 200):
    mensaje = "Area Pequeña"
# Si el area es >201 y <= 500 se considerara "Area Grande"
elif(area > 201) and (area <= 500):
    mensaje = "Area Grande"
# Si el area es superior a 500 se considerara area extensa
else:
    mensaje = "Area extensa"
#OUTPUT
print(area,mensaje)
#fin_if

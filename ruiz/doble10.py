# Programa 10
import os
#Declaracion de variables
x=0
y=0
mensaje=""
#Input via OS
x=(os.sys.argv[1])
y=(os.sys.argv[2])
#Si x < y decir que es menor que
if x < y:
    mensaje = "es menor que"
#Si x > y decir que es mayor que
else:
    mensaje = "es mayor que"
#Output
print(x,mensaje,y)
#fin_if

# Programa 10
import os
#Declaracion de variables
x=0
y=0
mensaje=""
#Input via OS
x=(os.sys.argv[1])
y=(os.sys.argv[2])
#Si x < y decir que x es menor que y
if ( x < y ) :
    mensaje = "es menor que"
#Si x > y decir que x es mayor que y
elif ( x > y) :
    mensaje = "es mayor que"
#Si x == y decir que x es igual que y
else:
    mensaje = "es igual que"
#Output
print(x,mensaje,y)
#fin_if

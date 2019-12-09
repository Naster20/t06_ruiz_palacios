#PROGRAMA 1
#Ejercicio 1 condicional simple
import os
n1,n2,n3,n4,prom,mensaje=0,0,0,0,0,""
#INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])
#PROCESSING
prom=int((n1+n2+n3+n4)/4)
#Si el promedio obtenido supera los 85 puntos
#mostrar good job
if  (prom>85):
    mensaje="Good job"
#OUTPUT
print(mensaje)
#finif

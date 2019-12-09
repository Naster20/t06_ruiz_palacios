#PROGRAMA 19
#Ejercicio 19 condicional doble
import os
edad,nombre,nota1,nota2=0,"",0.0,0.0
#INPUT VIA OS
edad=int(os.sys.argv[1])
nombre=os.sys.argv[2]
nota1=float(os.sys.argv[3])
nota2=float(os.sys.argv[4])
#PROCESSSING
#Si el promedio supera 10 de nota
#mostrar "aprobado"
prom=(nota1+nota2)/2
esta_aprobado=(prom>10)
if(esta_aprobado):
    print("El alumno",nombre,"esta aprobado")
else:
    print("El alumno",nombre,"esta desaprobado")
#finif

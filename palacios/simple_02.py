#PROGRAMA 2
#Ejercicio 2 condicional simple
import os
usuario,Clave="",""
#INPUT VIA OS
usuario=os.sys.argv[1]
clave=os.sys.argv[2]
#processing
#Si el usuario es "admin"
#y la clave es "$#r" mostrar "acceso ok"
if(usuario=="admin")and(clave=="$#r"):
    print("Acceso ok")
#finif

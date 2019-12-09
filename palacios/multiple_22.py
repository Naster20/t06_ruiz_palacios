#PROGRAMA 22
#Ejercicio 22 condicional multiple
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
if(usuario=="lewis")and(clave=="1234"):
    print("Acceso ok")
#finif

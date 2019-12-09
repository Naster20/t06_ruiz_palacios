# Programa 01
import os
#DECLARACION DE VARIABLES
usuario=""
mensaje=""
#INPUT VIA OS
usuario=os.sys.argv[1]
#PROCESSING
#Si el usuario es igual a "Ruiz" mostrar Administrador reconocido
if(usuario == "Ruiz"):
    mensaje = "Administrador Reconocido"
elif(usuario == "Fernando"):
    mensaje = "Posible Admisitrador"
elif( usuario == "Claudio"):
    mensaje = "No tienes acceso"
else:
    mensaje = "Revise datos"
#OUTPUT
print(mensaje)
#fin_if

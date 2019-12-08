# Programa 08
import os
#Declaracion de variables
nro_ejercicios=0
ejercicios_resuelos=0

#Input via OS

nro_ejercicios=int(os.sys.argv[1])
ejercicios_resuelos=int(os.sys.argv[2])

#Processing
if (ejercicios_resuelos < 20):
    print("DESAPROBADO")

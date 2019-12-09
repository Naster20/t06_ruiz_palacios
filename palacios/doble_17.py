#PROGRAMA 17
#Ejercicio 17 condicional doble
import os
nro_correos_recibidos=0
#INPUT VIA OS
nro_correos_recibidos=int(os.sys.argv[1])
#processing
#Si supera los 1000 correos
#cobrar 2 soles por cada correo
correos_excesos=(nro_correos_recibidos-1000)*2
if(correos_excesos>0):
    print("Usted debe pagar",correos_excesos)
else:
    print("Usted no pagara exceso")
#finif

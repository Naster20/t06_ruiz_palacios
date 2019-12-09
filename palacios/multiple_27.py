#PROGRAMA 27
#Ejercicio 27 condicional multiple
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
if(correos_excesos<0):
    print("pagar la mitad de su recibo")
#finif

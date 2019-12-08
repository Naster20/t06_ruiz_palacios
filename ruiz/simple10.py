# Programa 10
import os
#Declaracion de variables
nro_correos_recibidos=0

#Input via OS
nro_correos_recibidos=int(os.sys.argv[1])

#Processing
correos_exceso=(nro_correos_recibidos-1000)*2

if(correos_exceso > 0):
    print("usted debera pagar S/.",correos_exceso,"soles")

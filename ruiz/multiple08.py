# Programa 08
import os
#Declaracion de variables
nro_ejercicios=0
ejercicios_resuelos=0
mensaje=""
#Input via OS
nro_ejercicios=int(os.sys.argv[1])
ejercicios_resuelos=int(os.sys.argv[2])
#Processing
# Si los ejercicios resuletos >0 and <=25 se le considerara "MALO"
if (ejercicios_resuelos > 0) and (ejercicios_resuelos <= 25 ):
    mensaje="MALO"
# Si los ejercicios resuletos >25 and <=50 se le considerara "REGULAR"
elif (ejercicios_resuelos > 25) and (ejercicios_resuelos <=50 ):
    mensaje="REGULAR"
# Si los ejercicios resuletos >50 and <=75 se le considerara "BUEN0"
elif (ejercicios_resuelos > 50) and (ejercicios_resuelos <=75 ):
    mensaje="BUENO"
# Si los ejercicios resuletos son >=75 se le considerara "EXCELENTE"
else:
    mensaje="EXCELENTE"
#Output
print("Numero de Ejercicios :",nro_ejercicios,",""Ejercicios Resueltos : ",ejercicios_resuelos,",""Condicion :",mensaje)
#fin_if

# Programa 05
import os
#Declaracion de variables
atleta=""
peso_antes_de_entrenamiento=0.0
peso_despues_de_entrenamiento=0.0
#Input via os
atleta=os.sys.argv[1]
peso_antes_de_entrenamiento=float(os.sys.argv[2])
peso_despues_de_entrenamiento=float(os.sys.argv[3])
#processing
diferencia_peso=(peso_antes_de_entrenamiento-peso_despues_de_entrenamiento)
# Si la diferencia de peso es mayor de 7kg entonces fue un excelente entrenamiento
if(diferencia_peso > 7):
    print("Excelente entrenamiento")
#Fin_if


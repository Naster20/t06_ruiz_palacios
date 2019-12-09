# Programa 05
import os
#Declaracion de variables
atleta=""
peso_antes_de_entrenamiento=0.0
peso_despues_de_entrenamiento=0.0
mensaje=""
#Input via os
atleta=os.sys.argv[1]
peso_antes_de_entrenamiento=float(os.sys.argv[2])
peso_despues_de_entrenamiento=float(os.sys.argv[3])
#processing
diferencia_peso=(peso_antes_de_entrenamiento-peso_despues_de_entrenamiento)
# Si la diferencia de peso es > 0 y <=3 entonces fue un Pesimo entrenamiento
if(diferencia_peso > 0) and (diferencia_peso <= 3):
    mensaje = "Pesimo Entrenamiento"
# Si la diferencia de peso es > 3 y <=8 entonces fue un Buen entrenamiento
elif(diferencia_peso > 3) and (diferencia_peso <= 8):
    mensaje = "Buen Entrenamiento"
# Si la diferencia de peso es mayor de 8kg entonces fue un excelente entrenamiento
else:
    mensaje = "Excelente Entrenamiento"
#Output
print(atleta,"perdiste",diferencia_peso,"Kg",mensaje)
#fin_if

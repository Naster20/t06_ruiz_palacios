# Programa 09
import os
#Declaracion de variables
monto=0.0
sector=""
descuento1=0.0
# Input via OS
monto=float(os.sys.argv[1])
sector=(os.sys.argv[2])
# Processing
descuento1 = float(monto*0.3)
descuento2 = float(monto*0.4)
#Si su monto es >=300 y <= 500
# Y es del sector "Publico" se le aplicara un descuento del 30%
if (monto >= 300) and (monto <=500 ) and (sector == "Publico"):
    print("Su descuento es de :",descuento1,"Soles")
    mensaje = "Su descuento es del 30%"
#Si su monto es >500 y <= 1000
# Y es del sector "Publico" se le aplicara un descuento del 30%
elif (monto > 500) and (monto <=1000 ) and (sector == "Publico"):
    print("Su descuento es de :",descuento2,"Soles")
    mensaje = "Su descuento es del 40%"
#Si no cumple con las condiciones antes mencionda no tendra descuento
else:
    mensaje = "No tiene descuento"
# Output
print("Monto bruto:",monto,",",mensaje)
#fin_if

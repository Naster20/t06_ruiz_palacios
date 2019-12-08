# Programa 09
import os
#Declaracion de variables
monto=0.0
sector=""
descuento=0.0
# Input via OS
monto=float(os.sys.argv[1])
sector=(os.sys.argv[2])
# Processing
descuento = float(monto*0.3)
#Si su monto es superior e igual a 300
# Y es del sector publico se le aplicara un descuento del 30%
if (monto >= 300) and (sector == "Publico"):
    mensaje = "Su descuento es del 30%"
#Si no cumple con las condiciones antes mencionda no tendra descuento
else:
    mensaje = "No tiene descuento"
# Output
print("Monto bruto:",monto,",",mensaje)
#fin_if

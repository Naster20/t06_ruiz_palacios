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
descuento=float(monto*0.3)
if (sector == "Publico"):
    print(descuento)


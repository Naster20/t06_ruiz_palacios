#PROGRAMA 24
#Ejercicio 24 condicional multiple
import os
tickets=0
#INPUT VIA OS
tickets=int(os.sys.argv[1])
#processing
#ganaste_un_caramelo=nro_de_tickets>100
if(tickets>200):
    print("Ganaste dos caramelo")
if(tickets>100)and (tickets<200):
    print("Ganaste un caramelo")
#finif

from random import randint 

lista =[]

for i in range(3):
    lista.append(randint(0,100))
print lista
#booleano inicializado en falso
adivinado = False
"""
ciclo que permite 5 opciones
verifica si el numero esta en la lista
"""
for i in range(5):
    a =input(" Ingrese su valor " )
    if a in lista:
        print "ganaste"
        adivinado = True
        break
    else:
        print "Sigue Intentando "
        
if not adivinado:
    cad = " "
    for i in lista:
        cad += str(i) + ", "
    print " El numero aleatorio fue : " + cad[:-2]
  

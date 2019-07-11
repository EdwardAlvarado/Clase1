from random import randint

def generar numero():
    lista =[]
    a=0
    for i in range(10):
        x=randint(0,10)
        if x in lista:
            print "numero repetido"
        else:
        lista.append(x)
        if len(lista)==3:
            break
     
print lista

def captura (tam)
lista1 =raw_input ("Ingrese un numero de tres cifras: ")
list (lista1)
digitos = [int(x) for x in list(lista1)]
print digitos

def validar_repetido()
for i in range(len(digitos)):
    if i in digitos:
        print "numero repetido"
    else:
        lista.append(digitos[i])
    if len(lista)==3:
        break
print lista

def comparar (lista1, lista2):
    p=0
    f=0
    for i in range(len(lista1)):
        if l1[i] in l2:
            f += 1
        else:
            p += 1
    return f,p
        


       
print lista


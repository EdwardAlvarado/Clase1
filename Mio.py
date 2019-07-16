from random import randint

def genera_aleatorio(tam):
    lista = []
    while len(lista) < tam :
        x = randint (1,9)
        if x not in lista:
            lista.append (x)
    return lista

def captura_numero(tam):
    lista = []
    while len(lista) != tam:
        lista = [int(x) for x in list( raw_input(" Ingrese un entero de " + str(tam) + " digitos "))]
    return lista

def comparar (lista1, lista2):
    pica = 0
    fija = 0
    for i in range (len(lista1)):
        if lista1[i] in lista2:
            if lista1[i] == lista2[i]:
                fija += 1
            else:
                pica +=1
    return fija, pica

def  gana (num,alea):
    if i ==a :
        print "gano"

def intentos (alea,inten):
    intentos=0
    listatotal = []
    while intentos < inten:
        ing = captura_numero(3)
        fija, pica = comparar (alea, ing)
        print "usted tiene " + str(fija) + " Fijas " + str(pica) + " Picas "
        listatotal.append([ing,fija,pica])
        if fija == 3:
            print "****************"
            print "*  GANANDOR    *"
            print "****************"
            print "                "
            print " El numero ganador es " + str(alea)
            print "                " 
            break
        intentos =intentos+1
       
    return listatotal
        
    

intento=5
ale = genera_aleatorio(3)
print ale
resultados = intentos(ale,intento)
for i in resultados:
    print " El numero ingresado es: " + str(i[0]) + " Tuvo " + str(i[1]) + " Fijas " + str(i[2]) + " Picas "
print " **************** "
print " El Numero a adivinar es : " + str(ale)

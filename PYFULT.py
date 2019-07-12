from random import randint

def genera_aleatorio(tam):
    lista = []
    while len(lista) < tam:
        a = randint(1,9)
        if a not in lista:
            lista.append(a)
    return lista

def captura_numero(tam):
    lista = []
    while len(lista) != tam:
        lista = [int(x) for x in list(raw_input("Ingrese un entero de " + str(tam) + " digitos: "))]
    return lista


def comparar (l1, l2):
    pica = 0
    fija = 0
    for i in range (len (l1)):
        if l1 [i] in l2:
            if l1 [i] == l2 [i]:
                fija += 1
            else:
                pica += 1
    return fija, pica
                
    

def gana(i, a):
    if i == a:
        print "gano "

ale = genera_aleatorio(3)
print ale
ing = captura_numero(3)
print comparar (ale, ing)
fija, pica = comparar (ale, ing)
print " fijas = " + str (fija) + " pica = " + str (pica)

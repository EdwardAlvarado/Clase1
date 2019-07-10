from random import randint 

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


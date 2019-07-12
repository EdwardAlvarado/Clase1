from Figuras import *

p1 = Punto(5,5)
p2 = Punto(5,10)
p3 = Punto(10,1)
cuadrado = Cuadrado(p1, p2)
circulo = Circulo(p1, p2)
triangulo = Triangulo (p1, p3)


cuadrado.calcular_area()
circulo.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_perimetro()
triangulo.calcular_area()

print " El area del cuadrado es :" + str(cuadrado.area)
print " El area del circulo es :" + str(circulo.area)
print " El perimetro del cuadrado es :" + str(cuadrado.perimetro)
print " El perimetro del circulo es :" + str(circulo.perimetro)
print " El area del triangulo es :" + str(triangulo.area)

from math import *
from Punto import *


class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.fin = p2
        self.area = 0
        self.perimetro = 0

class Cuadrado(Figura):

    
    def calcular_area(self):
        lado=self.origen.calcular_distancia(self.fin)
        self.area = lado * lado

    def calcular_perimetro(self):
        lado=self.origen.calcular_distancia(self.fin)
        self.perimetro = lado + lado + lado +lado 
        
    
class Circulo (Figura):


    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = pi * (radio ** 2)

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = (2 * pi) * radio

class Triangulo(Figura):

    def calcular_area(self):
        p=Punto(self.origen.x,self.fin.y)
        base=p.calcular_distancia(self.fin)
        alt=p.calcular_distancia(self.origen)
        self.area=(base * alt) / 2
        


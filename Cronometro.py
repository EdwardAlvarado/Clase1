class UnidadT():
    def __init__(self):
        self.valori = 0
        self.max = 0

    def iniciar(self, inicial):
        self.valori = inicial

    def avanzar(self):
        self.valori +=1
        if self.valori >= self.max:
            self.valori = 0

    def reiniciar (self, nuevo):
        self.valori = 0

class Hora(UnidadT):

    def __init__(self):

        self.valori = 0
        self.max = 23

class Minuto(UnidadT):

    def __init__(self):

        self.valori = 0
        self.max = 59


class Segundo(UnidadT):

    def __init__(self):

        self.valori = 0
        self.max = 59


class Cronometro():

    def __init__(self):
        self.hora = Hora()
        self.minuto = Minuto()
        self.segundo = Segundo()

    def iniciarCrono(self, iniciales):
        self.hora.iniciar(iniciales[0])
        self.minuto.iniciar(iniciales[1])
        self.segund0.iniciar(iniciales[2])

    def avanzarCrono (self):
        self.segundo.avanzar()
        if self.segundo.valor == self.segundo.max:
            self.minuto.avanzar()
            if self.minuto.valor == self.minuto.max:
                self.hora.avanzar()

    def reiniciarCrono (self, iniciales):

        self.hora.reiniciar([0])
        self.minuto.reiniciar([1])
        self.segundo.reinicar([2])

    def mostraCrono(self):

        return str(self.hora.valori) + " : " + str(self.minuto.valori) + " : " + str(self.segundo.valori)
        
    
    
    

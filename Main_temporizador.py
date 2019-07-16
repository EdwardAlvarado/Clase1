from Temporizador import Temporizador
from time import sleep

t = Temporizador()

t.iniciar([0,1,15])

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.3)
    if tiempo == "0 : 0 : 0":
        break
    t.retroceder ()


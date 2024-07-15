from djitellopy import tello
import ModuloPresionTeclas
from time import sleep

ModuloPresionTeclas.init()
dron = tello.Tello()
dron.connect()
print(dron.get_battery())

#Funcion para quedarnos con las teclas pulsadas
def getTeclaEntrada():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50 #Velocidad de movimiento

    #Comprobar las teclas pulsadas y actualizo valores movimiento
    if ModuloPresionTeclas.getKey("LEFT"):
        lr = -speed
    elif ModuloPresionTeclas.getKey("RIGHT"):
        lr = speed
    elif ModuloPresionTeclas.getKey("UP"):
        fb = speed
    elif ModuloPresionTeclas.getKey("DOWN"):
        fb = -speed
    elif ModuloPresionTeclas.getKey("w"):
        ud = speed
    elif ModuloPresionTeclas.getKey("s"):
        ud = -speed
    elif ModuloPresionTeclas.getKey("a"):
        yv = speed
    elif ModuloPresionTeclas.getKey("d"):
        yv = -speed
    elif ModuloPresionTeclas.getKey("x"):
        yv = dron.flip_back()

    #Comandos aterrizar y despegar
    if ModuloPresionTeclas.getKey("q"):
        dron.land()
        dron.end()
    if ModuloPresionTeclas.getKey("t"):
        dron.takeoff()
    return [lr, fb, ud, yv]
#Bucle ppal del programat
while True:
    valores = getTeclaEntrada()
    dron.send_rc_control(valores[0], valores[1], valores[2], valores[3])
    sleep(0.05)
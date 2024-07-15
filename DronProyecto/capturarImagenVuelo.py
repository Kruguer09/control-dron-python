from djitellopy import tello
import ModuloPresionTeclas

import time
import cv2

ModuloPresionTeclas.init()
dron=tello.Tello()
dron.connect()
print(dron.get_battery())

dron.streamon()#inicia transmisión de video desde el dronwwwwwwwwwwwwwwwwww


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
        yv = -speed
    elif ModuloPresionTeclas.getKey("d"):
        yv = speed
    elif ModuloPresionTeclas.getKey("x"):
        yv = dron.flip_back()

    #Comandos aterrizar y despegar
    if ModuloPresionTeclas.getKey("q"):
        dron.land()
        dron.end()
    if ModuloPresionTeclas.getKey("t"):
        dron.takeoff()
    if ModuloPresionTeclas.getKey("f"):
        cv2.imwrite(f'Recursos/Imagenes/{time.time()}.jpg', img)
        time.sleep(0.05)
    return [lr, fb, ud, yv]

while True:
    valores = getTeclaEntrada()
    dron.send_rc_control(valores[0], valores[1], valores[2], valores[3])

    #Captura una imagen de video de mi dron
    img=dron.get_frame_read().frame
    img=cv2.resize(img,(640,480))
    #mostramos en una ventana
    cv2.imshow('Imagen',img)
    cv2.waitKey(1)#Espera un milisegundo para comprobar si se presiono alguna tecla

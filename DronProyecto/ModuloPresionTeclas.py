import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400)) #Establece el tamaño de ventana

#Funcion para comprobar que una tecla está pulsada
def getKey(keyName):
    respuesta = False
    for evento in pygame.event.get():
        pass #No hace nada aquí
    #Obtener es estado de las teclas
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName)) #Obtenemos el código

    #Comprobamos si la tecla que le paso está siendo pulsada
    if keyInput [myKey]:
        respuesta = True
    pygame.display.update() #Actualizo la ventana
    return respuesta

def main():
    if getKey("LEFT"): #Comprueba si la tecla izquierda está pulsada
        print("Izquierda pulsada")
    if getKey("RIGHT"): #Ídem con la dcha.
        print("Derecha pulsada")

if __name__ == '__main__':
    init()
    while True:
        main()


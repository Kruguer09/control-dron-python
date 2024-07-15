# importamos módulo tello de djitellopy
from djitellopy import tello
# creamos la instancia de la clase Tello
dron=tello.Tello()
#mostramos la información DE LA BATERÍA
#print(dron.get_battery())
# conectamos con el dron
dron.connect()
# despegamos
dron.takeoff()
# giro 360 grados
dron.rotate_clockwise(360)
dron.flip_back()

# avanzamos 100 cm
#dron.move_forward(100)
#giro a la izquierda 90 grados
#dron.rotate_counter_clockwise(90)
# avanzamos 100 cm
#dron.move_forward(100)
#giro a la izquierda 90 grados
#dron.rotate_counter_clockwise(90)
# avanzamos 100 cm
#dron.move_forward(100)
#giro a la izquierda 90 grados
#dron.rotate_counter_clockwise(90)

# aterrizamos
dron.land()
# desconectamos para liberear recursos
dron.end()

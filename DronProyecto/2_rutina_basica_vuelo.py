# importamos módulo tello de djitellopy
from djitellopy import tello
def rutina_basica_vuelo(dron):
    dron.connect()
    dron.takeoff()
    #dron.move_forward(20)
    #dron.move_back(20)
    #dron.move_right(20)
    #dron.move_left(20)
    #dron.move_up(20)
    #dron.move_down(20)
    dron.move_up(50)
    dron.flip_forward()
    dron.flip_back()
    dron.flip_left()
    dron.flip_right()
    dron.flip("f")

    dron.land()
    dron.end()


def main():
    dron=tello.Tello()
    rutina_basica_vuelo(dron)

if __name__== "__main__":
    main()
# importamos módulo tello de djitellopy
from djitellopy import tello
from time import sleep
def movimientosBasicos(dron):
    dron.connect()
    dron.takeoff()
    print(dron.get_battery())
    dron.send_rc_control(0,50,0,0)
    sleep(2)
    dron.send_rc_control(0, 0, 0, 30)
    sleep(2)
    dron.send_rc_control(0, 0, 0, 0)
    dron.land()


    #dron.move_forward(20)
    #dron.move_back(20)
    #dron.move_right(20)
    #dron.move_left(20)
    #dron.move_up(20)
    #dron.move_down(20)
    #dron.move_up(50)
    #dron.flip_forward()
    #dron.flip_back()
    #dron.flip_left()
    #dron.flip_right()
    #dron.flip("f")

    #dron.land()

    #dron.end()


def main():
    dron=tello.Tello()
    movimientosBasicos(dron)

if __name__== "__main__":
    main()
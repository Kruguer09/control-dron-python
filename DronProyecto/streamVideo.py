import cv2
from djitellopy import tello
def procesamiento_tello_vuelo(dron):
    while True:
        frame=dron.get_frame_read().frame
        cv2.imshow("Ventana", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            dron.move_forward(20)
            break
    cv2.destroyAllWindows()
    dron.streamoff()
    dron.end()

def main():
    dron = tello.Tello()
    dron.connect()
    #activamos la cámara
    dron.streamon()
    procesamiento_tello_vuelo(dron)

    if __name__ == "__main__":
        main()
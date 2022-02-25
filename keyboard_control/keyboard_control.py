from multiprocessing.connection import wait
from djitellopy import tello
import keyboard_control.keypress as kp
from time import sleep
import cv2

kp.init()
me = tello.Tello()
me.connect()
me.stream_on()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.get_key('LEFT'):
        lr = -speed
    elif kp.get_key('RIGHT'):
        lr = speed
    if kp.get_key('UP'):
        fb = speed
    elif kp.get_key('DOWN'):
        fb = -speed
    if kp.get_key('w'):
        ud = speed
    elif kp.get_key('s'):
        ud = -speed
    if kp.get_key('a'):
        yv = -speed
    elif kp.get_key('d'):
        yv = speed
    if kp.get_key('q'):
        me.land()
        sleep(3)
    if kp.get_key('e'):
        me.takeoff()
    return [lr, fb, ud, yv]

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow('Frame', img)
    cv2.waitKey(1)
    vals = getKeyboardInput()
    print(vals)
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

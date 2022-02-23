from djitellopy import tello
import keyboard_control.keypress as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()

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
    vals = getKeyboardInput()
    print(vals)
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

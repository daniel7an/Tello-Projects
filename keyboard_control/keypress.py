import pygame
from time import sleep

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def get_key(keyName):
    ans = False
    for event in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed() # returns an array of boolean values 
    myKey = getattr(pygame, 'K_{}'.format(keyName)) # get the key index in keyInput array
    #print('K_{}'.format(keyName))
    if keyInput[myKey]:# checking index of key in array (True or False)
        ans = True

    pygame.display.update()
    return ans

def getKeyboardInput(me):
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if get_key('LEFT'):
        lr = -speed
    elif get_key('RIGHT'):
        lr = speed
    if get_key('UP'):
        fb = speed
    elif get_key('DOWN'):
        fb = -speed
    if get_key('w'):
        ud = speed
    elif get_key('s'):
        ud = -speed
    if get_key('a'):
        yv = -speed
    elif get_key('d'):
        yv = speed
    if get_key('q'):
        me.land()
        sleep(3)
    if get_key('e'):
        me.takeoff()
    return [lr, fb, ud, yv]

def main():
    if get_key('a'):
        print('Left key pressed.')
        
    if get_key('d'):
        print('Right key pressed.')
        
if __name__ == '__main__':
    init()
    while True:
        main()
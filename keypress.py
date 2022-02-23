import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def get_key(keyName):
    ans = False
    for event in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    #print('K_{}'.format(keyName))

    if keyInput[myKey]:
        ans = True

    pygame.display.update()
    return ans

def main():
    if get_key('a'):
        print('Left key pressed.')
        
    if get_key('d'):
        print('Right key pressed.')
        

if __name__ == '__main__':
    init()
    while True:
        main()
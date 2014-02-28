import pygame
from pygame.locals import *
class KeyboardController:

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.registerListener(self)
        pygame.init()
        pygame.key.set_repeat(1, 10)
        self.jumpstarted = 0

    def Notify(self, event):
        ev=None
        if event=="TickEvent":
            self.evManager.post('Gravity')
            self.evManager.post('Enemy')
            if self.jumpstarted!=0:
                evj = "Jump"
                key = pygame.key.get_pressed()
                if key[K_RIGHT]:
                    evj="JumpRight"
                if key[K_LEFT]:
                    evj="JumpLeft" 
                self.evManager.post(evj)
                self.jumpstarted +=1
                if self.jumpstarted==10:
                    self.jumpstarted=0
                    self.evManager.post('Stopjump')
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_LEFT:
                    direction = "DIRECTION_LEFT"
                    ev = "LeftRequest"
                if event.type == QUIT:
                    ev = QuitEvent()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    ev = QuitEvent()
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    ev = "RightRequest" 
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if self.jumpstarted==0:
                        self.jumpstarted = 1
                    """ev = "UpRequest"
                    print 'upreq'
                    key = pygame.key.get_pressed()
                    if key[K_RIGHT]:
                        ev="RightUpRequest"
                        print 'here'
                    if key[K_LEFT]:
                        ev="LeftUpRequest" """
                if event.type == KEYDOWN and event.key == K_DOWN:
                    ev='DownRequest' 
                                                                 
        if ev:
            self.evManager.post( ev )

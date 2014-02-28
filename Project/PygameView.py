import pygame
from pygame.locals import *
import Game
class PygameView:
    def __init__(self, evManager,game):
        self.evManager = evManager
        self.evManager.registerListener( self )
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((600,400),DOUBLEBUF)
        self.screen.set_alpha(None)
        
        self.sector = self.game.mappe.sectors[0]
        self.sectorimg = pygame.image.load(self.sector.image)
        self.screen.blit(self.sectorimg,[0,0,600,400])
        
        self.character = self.game.charactor
        self.charimage = pygame.image.load(self.character.image)
        
        self.enemimages = []
        
        self.charrect = self.charimage.get_rect()
        self.charrect.topleft = (self.character.x,self.character.y)
        
        
        enemies = self.sector.enemies
        for enemy in enemies:
            enemimage = pygame.image.load(enemy.image)
            self.enemimages.append(enemimage)
            
        pygame.display.flip()

		
    def Notify(self, event):
        if event == "TickEvent":
                        
            self.screen.blit(self.sectorimg,self.charrect,self.charrect)
            self.screen.blit(self.sectorimg,[0,0,600,400])
<<<<<<< HEAD
            self.screen.blit(self.charimage,self.charrect)

            # display Rewards
            font = pygame.font.Font(None, 36)
            text = font.render('Munition: ' + str(self.character.rewardcount), 1, (10, 10, 10))
            textpos = text.get_rect(centerx=self.screen.get_width()/2)
            self.screen.blit(text, textpos)
=======
            if self.character.isalive:
                print 'alive'
                self.screen.blit(self.charimage,self.charrect)
            else:
                print 'dead'
            
>>>>>>> fa2bdd049ba40796b137ebefd948c94b4bc6d248
            
            enemies = self.sector.enemies
            for i in range(len(enemies)):
                enemimage = self.enemimages[i]
                enemrect = enemimage.get_rect()
                enemrect.topleft = (enemies[i].x,enemies[i].y)
                self.screen.blit(self.sectorimg,enemrect,enemrect)
                self.screen.blit(enemimage,enemrect)
            
            
            
            obstacles = self.sector.obstacles
            for obst in obstacles:
                obstimage = pygame.image.load(obst.image)
                obstrect = obstimage.get_rect()
                obstrect.topleft = (obst.x,obst.y)
            
                self.screen.blit(obstimage, obstrect)

            rewards = self.sector.rewards
            for rew in rewards:
                rewimage = pygame.image.load(rew.image)
                rewrect = rewimage.get_rect()
                rewrect.topleft = (rew.x,rew.y)

                self.screen.blit(rewimage, rewrect)
            
            pygame.display.flip()
    
        if event == 'MoveEvent':
            self.charrect.topleft = (self.character.x,self.character.y)

            
            

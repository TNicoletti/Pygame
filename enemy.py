import pygame
import math
import random

class Enemy(object):
    def __init__(self, x, y, player, platforms, s, bullets):
        self.x = x
        self.y = y
        self.width  = int(s/16) #50 #TODO dinamic
        self.height = int(s/16) #50 #TODO dinamic
        self.xVel = int(s*3/800) #TODO dinamic
        self.yVel = 0    #TODO dinamic

        self.tickTime = 0
        self.clockTick = 60

        self.scoreBonus = 50

        self.player = player

        self.bullets = bullets

        self.jumped = False
        self.jumpForce = -15 #TODO dinamic

        #self.landded = False

        self.platforms = platforms

        #self.g = gravity

        #self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.life = 200

        self.attackCool = 0

    def draw(self, win, s):      #TODO dinamic
        try:
            self.tickTime += 1
            if(self.tickTime % 30 < 15):
                image = self.IMAGE_0
            else:
                image = self.IMAGE_1
        except:
            self.tickTime = 0
            if(random.randint(0, 9) < 5):
                self.IMAGE_0 = pygame.transform.scale(pygame.image.load('./sprites/koi_azul_20.png'), (self.width, self.height))
                self.IMAGE_1 = pygame.transform.scale(pygame.image.load('./sprites/koi_azul_21.png'), (self.width, self.height))
            else:
                self.IMAGE_0 = pygame.transform.scale(pygame.image.load('./sprites/koi_vermelho_20.png'), (self.width, self.height))
                self.IMAGE_1 = pygame.transform.scale(pygame.image.load('./sprites/koi_vermelho_21.png'), (self.width, self.height))

            image = self.IMAGE_0
            self.tickTime = 0


        auxX = self.player.x - self.x
        auxY = self.player.y - self.y

        sen = 0
        try:
            sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))
        except:
            pass

        angle = math.degrees(math.asin(sen))

        if (auxX > 0):
            angle = 180 - angle

        if (angle < 0):
            angle = 360 + angle

        if(angle < 90 or angle > 270):
            image = pygame.transform.flip(image, 1, 0)

        '''if(self.ori == "right"):
            image = pygame.transform.flip(image, True, False)'''

        win.blit(image, (self.x, self.y))

        for x in self.bullets:
            x.draw(win, s)

    def move(self,s):

        self.tickTime += 1
        normalTime = self.tickTime / self.clockTick

        if(self.x > self.player.x):
            self.x -= self.xVel
            self.ori = "left"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x += self.xVel
                    if (not self.jumped):
                        self.yVel += self.jumpForce
                        self.jumped = True
                    break

        else:
            self.x += self.xVel
            self.ori = "right"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x -= self.xVel
                    if (not self.jumped):
                        self.yVel += self.jumpForce
                        self.jumped = True
                    break

        if(self.y < self.player.y):
            self.y += self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y -= self.xVel
                    break
        elif(self.y > self.player.y):
            self.y -= self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y += self.xVel
                    break

        if(normalTime % 1 == 0):
            self.attackCool += 1
        
    def confereMargem(self, *args):
        if(len(args) == 1):
            px = args[0].x
            py = args[0].y
            height = args[0].height
            width = args[0].width
        else:
            px = args[0].x
            py = args[1].y
            width = args[2].width
            height = args[3].height

        if(self.x + self.width > px and self.x < px + width):
            if(self.y + self.height > py and self.y < py + height):
                return True

        return False

    def takeDamage(self, damage,s):
        if(self.life <= 0):
            return

        self.life -= damage
        if(self.life <= 0):
            self.player.points += self.scoreBonus
            self.onDeath(s)
        else:
            self.player.points += 10

    def do_attack(self,s):

        if(self.confereMargem(self.player) and self.attackCool >= 1):
            self.player.takeDamage(1)
            self.attackCool = 0

    def onDeath(self,s):
        pass
import pygame
from spritesheet import *

from enemy import *

from math import sqrt, degrees, asin

from bullet import *

from items import *

import random

class TheFirstBoss(Enemy):
    def __init__(self, x, y, player, platforms,s, bullets):
        super().__init__(x, y, player, platforms,s, bullets)

        self.width = int(s/8)
        self.height = int(s/8)

        self.atualAttackCool = 7 * 60

        self.meleeCool = 0

        self.aux = 0

        self.mode = 0

        self.life = 4000

        self.DEFAULT_X = x
        self.DEFAULT_Y = y

        self.bullets = bullets

        self.SPRITES = SpriteSheet('./sprites/TheFirstBoss.png')

        self.IMAGE_STANDART_LU = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_LU = pygame.transform.scale(self.IMAGE_STANDART_LU, (self.width, self.height))

        self.IMAGE_STANDART_L = self.SPRITES.get_image(32, 0, 32, 32)
        self.IMAGE_STANDART_L = pygame.transform.scale(self.IMAGE_STANDART_L, (self.width, self.height))

        self.IMAGE_STANDART_LD = self.SPRITES.get_image(64, 0, 32, 32)
        self.IMAGE_STANDART_LD = pygame.transform.scale(self.IMAGE_STANDART_LD, (self.width, self.height))

        self.IMAGE_STANDART_RD = self.SPRITES.get_image(96, 0, 32, 32)
        self.IMAGE_STANDART_RD = pygame.transform.scale(self.IMAGE_STANDART_RD, (self.width, self.height))

        self.IMAGE_STANDART_R = self.SPRITES.get_image(0, 32, 32, 32)
        self.IMAGE_STANDART_R = pygame.transform.scale(self.IMAGE_STANDART_R, (self.width, self.height))

        self.IMAGE_STANDART_RU = self.SPRITES.get_image(32, 32, 32, 32)
        self.IMAGE_STANDART_RU = pygame.transform.scale(self.IMAGE_STANDART_RU, (self.width, self.height))



        self.IMAGE_SHOOTING_LU = self.SPRITES.get_image(64, 32, 32, 32)
        self.IMAGE_SHOOTING_LU = pygame.transform.scale(self.IMAGE_SHOOTING_LU, (self.width, self.height))

        self.IMAGE_SHOOTING_L = self.SPRITES.get_image(96, 32, 32, 32)
        self.IMAGE_SHOOTING_L = pygame.transform.scale(self.IMAGE_SHOOTING_L, (self.width, self.height))

        self.IMAGE_SHOOTING_LD = self.SPRITES.get_image(0, 64, 32, 32)
        self.IMAGE_SHOOTING_LD = pygame.transform.scale(self.IMAGE_SHOOTING_LD, (self.width, self.height))

        self.IMAGE_SHOOTING_RD = self.SPRITES.get_image(32, 64, 32, 32)
        self.IMAGE_SHOOTING_RD = pygame.transform.scale(self.IMAGE_SHOOTING_RD, (self.width, self.height))

        self.IMAGE_SHOOTING_R = self.SPRITES.get_image(64, 64, 32, 32)
        self.IMAGE_SHOOTING_R = pygame.transform.scale(self.IMAGE_SHOOTING_R, (self.width, self.height))

        self.IMAGE_SHOOTING_RU = self.SPRITES.get_image(96, 64, 32, 32)
        self.IMAGE_SHOOTING_RU = pygame.transform.scale(self.IMAGE_SHOOTING_RU, (self.width, self.height))


        self.IMAGE_ATTACK_11 = self.SPRITES.get_image(0, 96, 32, 32)
        self.IMAGE_ATTACK_11 = pygame.transform.scale(self.IMAGE_ATTACK_11, (self.width, self.height))

        self.IMAGE_ATTACK_12 = self.SPRITES.get_image(32, 96, 32, 32)
        self.IMAGE_ATTACK_12 = pygame.transform.scale(self.IMAGE_ATTACK_12, (self.width, self.height))


        self.IMAGE_ATTACK_20 = self.SPRITES.get_image(64, 96, 32, 32)
        self.IMAGE_ATTACK_20 = pygame.transform.scale(self.IMAGE_ATTACK_20, (self.width, self.height))

        self.IMAGE_ATTACK_21 = self.SPRITES.get_image(96, 96, 32, 32)
        self.IMAGE_ATTACK_21 = pygame.transform.scale(self.IMAGE_ATTACK_21, (self.width, self.height))

        self.IMAGE_ATTACK_22 = self.SPRITES.get_image(0, 128, 32, 32)
        self.IMAGE_ATTACK_22 = pygame.transform.scale(self.IMAGE_ATTACK_22, (self.width, self.height))

        self.IMAGE_ATTACK_23 = self.SPRITES.get_image(32, 128, 32, 32)
        self.IMAGE_ATTACK_23 = pygame.transform.scale(self.IMAGE_ATTACK_23, (self.width, self.height))

        self.IMAGE_ATTACK_24 = self.SPRITES.get_image(64, 128, 32, 32)
        self.IMAGE_ATTACK_24 = pygame.transform.scale(self.IMAGE_ATTACK_24, (self.width, self.height))

        self.IMAGE_ATTACK_25 = self.SPRITES.get_image(96, 128, 32, 32)
        self.IMAGE_ATTACK_25 = pygame.transform.scale(self.IMAGE_ATTACK_25, (self.width, self.height))

    def draw(self, win, s):  # TODO dinamic
        image = self.IMAGE_ATTACK_11
        if(self.mode == 0):

            x = self.player.x
            y = self.player.y

            xo = self.x + self.width/2
            yo = self.y + self.height/2

            auxX = xo - x
            auxY = yo - y

            sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))

            angle = degrees(asin(sen))

            if(auxX > 0):
                angle = 180 - angle

            if(angle < 0):
                angle = 360 + angle

            if(self.aux > 0):
                self.aux += 1
                if (angle <= 30 or angle >= 330):
                    image = self.IMAGE_SHOOTING_L
                elif (angle <= 90):
                    image = self.IMAGE_SHOOTING_LU
                elif (angle <= 150):
                    image = self.IMAGE_SHOOTING_RU
                elif (angle <= 210):
                    image = self.IMAGE_SHOOTING_R
                elif (angle <= 270):
                    image = self.IMAGE_SHOOTING_RD
                elif (angle <= 330):
                    image = self.IMAGE_SHOOTING_LD

                if(self.aux == 20):
                    self.aux = 0
            else:
                if (angle <= 30 or angle >= 330):
                    image = self.IMAGE_STANDART_L
                elif (angle <= 90):
                    image = self.IMAGE_STANDART_LU
                elif (angle <= 150):
                    image = self.IMAGE_STANDART_RU
                elif (angle <= 210):
                    image = self.IMAGE_STANDART_R
                elif (angle <= 270):
                    image = self.IMAGE_STANDART_RD
                elif (angle <= 330):
                    image = self.IMAGE_STANDART_LD
        elif(self.mode == 2):
            if(self.tickTime < 20):
                image = self.IMAGE_ATTACK_20
            elif(self.tickTime < 40):
                image = self.IMAGE_ATTACK_21
            elif(self.tickTime < 60):
                image = self.IMAGE_ATTACK_22
            else:
                if((self.tickTime % 60) < 20 ):
                    image = self.IMAGE_ATTACK_23
                    self.x = self.DEFAULT_X + 10
                    self.y = self.DEFAULT_Y
                elif((self.tickTime % 60) < 40):
                    image = self.IMAGE_ATTACK_24
                    self.x = self.DEFAULT_X - 10
                    self.y = self.DEFAULT_Y - 2
                elif((self.tickTime % 60) < 60):
                    image = self.IMAGE_ATTACK_25
                    self.x = self.DEFAULT_X - 5
                    self.y = self.DEFAULT_Y + 5

                r = random.randint(0, 2)

                if(r == 0):
                    self.x = self.DEFAULT_X + 10
                    self.y = self.DEFAULT_Y
                elif(r == 1):
                    self.x = self.DEFAULT_X - 10
                    self.y = self.DEFAULT_Y - 2
                elif(r == 2):
                    self.x = self.DEFAULT_X - 5
                    self.y = self.DEFAULT_Y + 5
        elif(self.mode == 1):
            if(self.tickTime % 20 < 10):
                image = self.IMAGE_ATTACK_11
            else:
                image = self.IMAGE_ATTACK_12
        win.blit(image, (self.x, self.y))

    def move(self, s):
        self.tickTime += 1

    def do_attack(self, s):
        '''if(self.tickTime > self.atualAttackCool):
            self.tickTime = 1
            rand = random.randint(0, 2)

            if(rand == 0):
                self.mode = 0
                self.atualAttackCool = 60 * 5
            elif(rand == 1):
                self.mode = 1
                self.atualAttackCool = 60 * 5
            elif(rand == 2):
                self.mode = 2
                self.atualAttackCool = 60 * 5'''

        if(self.life >= 3000):
            if(self.mode != 0):
                self.mode = 0
                self.tickTime = 0
        elif(self.life >= 2000):
            if(self.mode != 1):
                self.mode = 1
                self.tickTime = 0
        elif (self.life > 0):
            if (self.mode != 2):
                self.mode = 2
                self.tickTime = 0

        if (self.tickTime >= 60):
            if(self.mode == 0):

                if(self.tickTime % 30 == 0):
                    self.bullets.append(BulletTheFirstBoss(self.x + self.width/2, self.y + self.height/2, self.player.getX(), self.player.getY(), int(s*3/80), int(s*3/80), int(s*15/800), int(s/800)))
                    self.aux = 1

            elif(self.mode == 1):
                if(self.tickTime % 60 == 0):
                    r = random.randint(int(s/80), int(s*73/80))
                    self.bullets.append(BulletTheFirstBoss(int(s/80), r, self.player.x, self.player.y, int(s*2/80), int(s*2/80), int(s*6/800), int(s/800)))
                    self.bullets.append(BulletTheFirstBoss(int(s*77/80), r, self.player.x, self.player.y, int(s*2/80), int(s*2/80), int(s*6/800), int(s/800)))
            elif(self.mode == 2):

                #r = random.randint(0, )
                if(self.tickTime % (120) == 0):
                    self.bullets.append(BulletTheFirstBossVariatings(int(s*13/80), int(s/80), int(s*13/80), s, int(s*35/800), int(s*35/800), random.randrange(1, 5), 1))
                elif(self.tickTime % (120) == 40):
                    self.bullets.append(BulletTheFirstBossVariatings(int(s*39/80), int(s/80), int(s*39/80), s, int(s*35/800), int(s*35/800), random.randrange(1, 5), 1))
                elif(self.tickTime % 120 == 80):
                    self.bullets.append(BulletTheFirstBossVariatings(int(s*64/80), int(s/80), int(s*64/80), s, int(s*35/800), int(s*35/800), random.randrange(1, 5), 1))

                if (self.tickTime % 20 == 0):
                    self.bullets.append(BulletTheFirstBoss(int(s/80), int(s*75/80), int(s/80), 0, int(s*35/800), int(s*35/800), int(s*5/800), int(s/800)))
                    self.bullets.append(BulletTheFirstBoss(int(s*27/80), int(s*75/80), int(s*26/80), 0, int(s*35/800), int(s*35/800), int(s*5/800), int(s/800)))
                    self.bullets.append(BulletTheFirstBoss(int(s*51/80), int(s*75/80), int(s*5/8), 0, int(s*35/800), int(s*35/800), int(s*5/800), int(s/800)))
                    self.bullets.append(BulletTheFirstBoss(int(s*755/800), int(s*75/80), int(s*755/800), 0, int(s*35/800), int(s*35/800), int(s*5/800), int(s/800)))

        self.meleeCool += 1
        if (self.confereMargem(self.player) and self.meleeCool >= 60):
            self.player.takeDamage(1)
            self.meleeCool = 0

    def onDeath(self,s):
        self.player.items.append(firstItem(self.x, self.y, self.player,s))



class BulletTheFirstBoss(Bullet):
    def __init__(self, xo, yo, x, y, width, height, vel, damage):
        self.x = xo
        self.y = yo
        # self.xT = x
        # self.yT = y
        # self.m = (yo - y)/(xo - x)
        self.width = width
        self.height = height

        self.damage = damage

        self.vel = vel

        # self.xVel = (self.xT - self.x) / 10
        # self.yVel = (self.yT - self.y) / 10

        auxX = xo - x
        auxY = yo - y

        self.sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))
        self.cos = math.sqrt(1 - self.sen * self.sen)
        # print("sen:", self.sen)
        # print("cos:", self.cos)

        if (auxX < 0):
            self.xVel = self.cos * vel
        else:
            self.xVel = -self.cos * vel

        self.yVel = -self.sen * vel

        #print(self.xVel)
        #print(self.yVel)

        self.image = pygame.image.load('./sprites/tiro_2.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        d = degrees(asin(self.sen))

        if (auxX > 0):
            d = 180 - d
        # d -= 90

        '''if(d > 360):'''

        self.image = pygame.transform.rotate(self.image, d)

    def draw(self, win, s):
        if(self.x > 0  and self.y > 0 and self.x <= s and self.y <= s):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))

class BulletTheFirstBossVariatings(BulletTheFirstBoss):
    def __init__(self, xo, yo, x, y, width, height, vel, damage):
        super().__init__(xo, yo, x, y, width, height, vel, damage)

        self.towhere = 0

        self.INITIAL_X = x
        self.INITIAL_Y = y

    def move(self):
        super().move()

        if(self.towhere == 0):
            self.x += self.vel
            if(self.x - self.INITIAL_X >=  60):
                #print("a")
                self.towhere = 1
        elif(self.towhere == 1):
            self.x -= self.vel
            if (self.INITIAL_X - self.x >= 60):
                #print("b")
                self.towhere = 0

class firstItem(Item):
    def get(self, player):
        player.gunBuffROF = player.gunBuffROF/2
        player.buffGun()

        self.selfDestroy(player)
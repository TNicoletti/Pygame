import pygame
from spritesheet import *

from enemy import *

from math import sqrt, degrees, asin

from bullet import *


class TheFirstBoss(Enemy):
    def __init__(self, x, y, player, platforms):
        super().__init__(x, y, player, platforms)

        self.atualAttackCool = 0

        self.mode = 0

        self.life = 2000

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
        self.IMAGE_ATTACK_12 = pygame.transform.scale(self.IMAGE_ATTACK_11, (self.width, self.height))


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

    def draw(self, win):  # TODO dinamic
        image = 0
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
                self.angle = 180 - self.angle

            if(self.angle < 0):
                self.angle = 360 + self.angle

            if(self.angle >= 315 or self.angle <= 45):
                image = self.IMAGE_STANDART_R
            elif(self.angle >= 45 and self.angle <= 135):
                image = self.IMAGE_STANDART_RU
            elif(self.angle >= 135 and self.angle <= 225):
                image = self.IMAGE_STANDART_L
            else:
                image = self.IMAGE_STANDART_LD


        win.blit(image, (self.x, self.y))

        for x in self.bullets:
            x.draw(win)

    def move(self):
        self.tickTime += 1

    def do_attack(self):
        if(self.tickTime > self.atualAttackCool):
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
                self.atualAttackCool = 60 * 5

        if(self.mode == 0):

            if(self.tickTime % 60):
                self.bullets.append(BulletTheFirstBoss(self.x, self.y, self.player.x, self.player.y, 10, 10, 10, 1))

        elif(self.mode == 1):
            pass
        elif(self.mode == 2):
            pass



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

        self.hitbox = (self.x, self.y, self.width, self.height)

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

        self.image = pygame.image.load('./sprites/tiro_2.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        d = degrees(asin(self.sen))

        if (auxX > 0):
            d = 180 - d
        # d -= 90

        '''if(d > 360):'''

        self.image = pygame.transform.rotate(self.image, d)

    def draw(self, win):
        if(self.x > 0  and self.y > 0 and self.x <= 800 and self.y <= 800):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))
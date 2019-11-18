import pygame
from spritesheet import *

from enemy import *

from math import sqrt, degrees, asin

from bullet import *


class TheFirstBoss(Enemy):
    def __init__(self, x, y, player, platforms):
        super().__init__(x, y, player, platforms)

        self.SPRITES = SpriteSheet('./sprites/TheFirstBoss.png')

        self.IMAGE_STANDART_LU = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_LU = pygame.transform.scale(self.IMAGE_STANDART_LU, (self.width, self.height))

        self.IMAGE_STANDART_L = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_L = pygame.transform.scale(self.IMAGE_STANDART_L, (self.width, self.height))

        self.IMAGE_STANDART_LD = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_LD = pygame.transform.scale(self.IMAGE_STANDART_LD, (self.width, self.height))

        self.IMAGE_STANDART_RD = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_RD = pygame.transform.scale(self.IMAGE_STANDART_RD, (self.width, self.height))

        self.IMAGE_STANDART_R = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_R = pygame.transform.scale(self.IMAGE_STANDART_R, (self.width, self.height))

        self.IMAGE_STANDART_RU = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_STANDART_RU = pygame.transform.scale(self.IMAGE_STANDART_RU, (self.width, self.height))

    def draw(self, win):  # TODO dinamic
        image = self.IMAGE_STANDART_R

        auxX = self.player.x - self.x
        auxY = self.player.y - self.y

        sen = 0
        try:
            sen = (auxY) / (sqrt(auxX * auxX + auxY * auxY))
        except:
            pass

        angle = degrees(asin(sen))

        if (auxX > 0):
            angle = 180 - angle

        if (angle < 0):
            angle = 360 + angle

        image = pygame.transform.rotate(image, angle)

        '''if(self.ori == "right"):
            image = pygame.transform.flip(image, True, False)'''

        win.blit(image, (self.x, self.y))

        for x in self.bullets:
            x.draw(win)

    def move(self):

        self.tickTime += 1
        normalTime = self.tickTime / self.clockTick

        if (self.x > self.player.x):
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

        if (self.y < self.player.y):
            self.y += self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y -= self.xVel
                    break
        elif (self.y > self.player.y):
            self.y -= self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y += self.xVel
                    break

        if (normalTime % 1 == 0):
            self.attackCool += 1

        for x in self.bullets:
            x.move()

        toRemove = []

        for x in self.bullets:
            if(x.x < 0 or x.x > 800 or x.y < 0 or x.y > 800):
                toRemove.append(x)
                continue
            for p in self.platforms:
                if(p.confereMargem(x)):
                    toRemove.append(x)
                    break

        for x in toRemove:
            self.bullets.remove(x)

    def do_attack(self):
        if(self.tickTime > self.ATTACK_COOL):
            self.bullets.append(
            BulletPatoComArma(self.x + self.width / 2, self.y + self.height / 2, self.player.x, self.player.y, 15, 15, 10, 1))
            self.tickTime = 0

        toRemove = []
        for b in self.bullets:
            if(self.player.confereMargem(b)):
                self.player.takeDamage(b.damage)
                toRemove.append(b)

        for b in toRemove:
            self.bullets.remove(b)


class BulletPatoComArma(Bullet):
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
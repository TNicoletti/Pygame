import pygame
import math
from math import asin, degrees

class Bullet(object):
    def __init__(self, xo, yo, x, y, width, height, vel, damage):
        self.x = xo
        self.y = yo
        #self.xT = x
        #self.yT = y
        #self.m = (yo - y)/(xo - x)
        self.width  = width
        self.height = height

        self.damage = damage

        self.vel = vel

        #self.xVel = (self.xT - self.x) / 10
        #self.yVel = (self.yT - self.y) / 10

        self.hitbox = (self.x, self.y, self.width, self.height)

        auxX = xo - x
        auxY = yo - y

        self.sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))
        self.cos = math.sqrt(1 - self.sen*self.sen)
        #print("sen:", self.sen)
        #print("cos:", self.cos)

        if(auxX < 0):
            self.xVel = self.cos * vel
        else:
            self.xVel = -self.cos * vel

        self.yVel = -self.sen * vel

        self.image = pygame.image.load('./sprites/tiro_0.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        d = degrees(asin(self.sen))

        if (auxX > 0):
            d = 180 - d
        #d -= 90

        '''if(d > 360):'''

        self.image = pygame.transform.rotate(self.image, d)

    def draw(self, win):
        if(self.x > 0  and self.y > 0 and self.x <= 800 and self.y <= 800):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))


    def move(self):

        self.x += self.xVel
        self.y += self.yVel

        #self.x *= self.vel
        #self.y *= self.vel

        #self.x += self.vel
        #self.y = self.m * (self.x - self.xT) + self.yT
import pygame
from bullet import *

class Gun(object):
    def __init__(self, damage, rateOfFire, player):
        self.damage = damage
        self.rateOfFire = rateOfFire

        self.player = player

        self.cont = 0

        self.tickTime = 0
        self.clockTick = 60


    def shot(self, bullets, x, y):

        self.tickTime += 1

        self.cont += 1

        if(self.cont >= self.rateOfFire):
            self.cont = 0
            if(self.player.ori == "left"):
                bullets.append(Bullet(self.player.x, self.player.y, x, y, 4, 4, 10, self.damage))
            elif(self.player.ori == "right"):
                bullets.append(Bullet(self.player.x + self.player.width, self.player.y, x, y, 4, 4, 10, self.damage))

    def cool(self):
        self.tickTime += 1

        self.cont += 1
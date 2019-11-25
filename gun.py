import pygame
from bullet import *

class Gun(object):
    def __init__(self, damage, rateOfFire, shooter, name):
        self.damage = damage
        self.rateOfFire = rateOfFire

        self.shooter = shooter

        self.cont = 0

        self.tickTime = 0
        self.clockTick = 60

        self.name = name


    def shot(self, bullets, x, y):

        self.tickTime += 1

        self.cont += 1

        if(self.cont >= self.rateOfFire):
            self.cont = 0
            bullets.append(Bullet(self.shooter.x + self.shooter.width/2, self.shooter.y  + self.shooter.height/2, x, y, 25, 25, 10, self.damage))

    def cool(self):
        self.tickTime += 1

        self.cont += 1
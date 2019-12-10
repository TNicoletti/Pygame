import pygame

from enemy import *

from math import sqrt, degrees, asin

from bullet import *

class Patocomarma(Enemy):
    def __init__(self, x, y, player, platforms, s, bullets):
        self.x = x
        self.y = y
        self.width = int(s/16) #50  # TODO dinamic
        self.height = int(s/16)  # TODO dinamic
        self.xVel = int(s/400)  #2  # TODO dinamic
        self.yVel = 0  # TODO dinamic

        self.tickTime = 0
        self.clockTick = 60

        self.player = player

        self.jumped = False
        self.jumpForce = -15  # TODO dinamic

        # self.landded = False

        self.platforms = platforms

        # self.g = gravity

        # self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.life = 200

        self.attackCool = 0

        self.bullets = bullets

        self.ATTACK_COOL = 60

        self.scoreBonus = 60

        self.PATO_IMAGE = pygame.image.load('./sprites/patocomumaarma.png')
        self.PATO_IMAGE = pygame.transform.scale(self.PATO_IMAGE, (self.width, self.height))

    def draw(self, win, s):  # TODO dinamic
        image = self.PATO_IMAGE

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

    def move(self, s):

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

    def do_attack(self,s):
        if(self.tickTime > self.ATTACK_COOL):
            self.bullets.append(
            BulletPatoComArma(self.x + self.width / 2, self.y + self.height / 2, self.player.x, self.player.y, int(s*15/800), int(s*15/800), int(s/80), int(s/800)))
            self.tickTime = 0

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
        vel = self.vel

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

    def draw(self, win, s):
        if(self.x > 0  and self.y > 0 and self.x <= s and self.y <= s):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))
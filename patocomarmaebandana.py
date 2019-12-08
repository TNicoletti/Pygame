import pygame

from enemy import *

from math import sqrt, degrees, radians, sin, cos, hypot, pi

from bullet import *

class Patocomarmaebandana(Enemy):
    def __init__(self, x, y, player, platforms, s):
        self.x = x
        self.y = y
        self.width = int(s/16) #50  # TODO dinamic
        self.height = int(s/16)  # TODO dinamic
        self.xVel = int(s/400)   # TODO dinamic
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

        self.bullets = []

        self.ATTACK_COOL = 120

        self.scoreBonus = 60

        self.PATO_IMAGE = pygame.image.load('./sprites/patocomumaarmaebandana.png')
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

        for x in self.bullets:
            x.draw(win,s)

    def move(self,s):

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
            if(x.x < 0 or x.x > s or x.y < 0 or x.y > s):
                toRemove.append(x)
                continue
            for p in self.platforms:
                if(p.confereMargem(x)):
                    toRemove.append(x)
                    break

        for x in toRemove:
            self.bullets.remove(x)

    def do_attack(self,s):
        if(self.tickTime > self.ATTACK_COOL):
            auxX = (self.x + self.width / 2) - (self.player.x + int(s/16))
            auxY = (self.y + self.height / 2) - (self.player.y + int(s/16))

            sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))

            if (sen > 1):
                sen -= 1
            elif (sen < -1):
                sen += 1

            vel = int(s / 80)

            d = asin(sen)
            cosd = cos(d)*vel
            send = -sin(d)*vel

            d1 = d + pi/8
            if(d1 > 2*pi):
                d1 -= 2 * pi
            cosd1 = cos(d1) * vel
            send1 = -sin(d1) * vel

            d2 = d - pi/8
            if(d2 < 0):
                d2 += 2 * pi
            cosd2 = cos(d2) * vel
            send2 = -sin(d2) * vel

            if (auxX > 0):
                cosd = -cosd
                cosd1 = -cosd1
                cosd2 = -cosd2

            self.bullets.append(
                BulletPatoComArma(self.x + self.width / 2, self.y + self.height / 2, d, cosd, send, int(s*15/800),
                                  int(s*15/800), int(s/800)))

            self.bullets.append(
                BulletPatoComArma(self.x + self.width / 2, self.y + self.height / 2, d1,cosd1, send1, int(s*15/800),
                                  int(s*15/800), int(s/800)))

            self.bullets.append(
                BulletPatoComArma(self.x + self.width / 2, self.y + self.height / 2, d2,cosd2, send2, int(s*15/800),
                                  int(s*15/800), int(s/800)))

            self.tickTime = 0

        toRemove = []
        for b in self.bullets:
            if(self.player.confereMargem(b)):
                self.player.takeDamage(b.damage)
                toRemove.append(b)

        for b in toRemove:
            self.bullets.remove(b)


class BulletPatoComArma(Bullet):
    def __init__(self, xo, yo, d, xVel, yVel, width, height, damage):
        self.x = xo
        self.y = yo
        # self.xT = x
        # self.yT = y
        # self.m = (yo - y)/(xo - x)
        self.width = width
        self.height = height

        self.damage = damage
        # self.xVel = (self.xT - self.x) / 10
        # self.yVel = (self.yT - self.y) / 10

        self.hitbox = (self.x, self.y, self.width, self.height)

        # print("sen:", self.sen)
        # print("cos:", self.cos)

        self.xVel = xVel

        self.yVel = yVel

        self.image = pygame.image.load('./sprites/tiro_2.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.image = pygame.transform.rotate(self.image, d)

    def draw(self, win, s):
        if(self.x > 0  and self.y > 0 and self.x <= s and self.y <= s):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))
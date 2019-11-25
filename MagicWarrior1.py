import pygame
from spritesheet import *

from enemy import *

from math import sqrt, degrees, asin

from bullet import *

class MagicWarrior1(Enemy):
    def __init__(self, x, y, player, platforms, s):
        self.x = x
        self.y = y
        self.width = int(s*75/800) #75  # TODO dinamic
        self.height = int(s*75/800) #75  # TODO dinamic
        self.xVel = int(s/400) * 2 #2  # TODO dinamic
        self.yVel = 0  # TODO dinamic

        self.tickTime = 0
        self.clockTick = 60

        self.mode = "run"

        self.player = player

        self.jumped = False
        self.jumpForce = -15  # TODO dinamic

        # self.landded = False

        self.platforms = platforms

        self.bullets = []

        # self.g = gravity

        # self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.life = 750

        self.attackCool = 0

        bullets = []

        self.SPRITES = SpriteSheet('./sprites/MAGIC_WARRIOR_1.png')

        self.IMAGE_FRONT_WALKING_IDLE = self.SPRITES.get_image(0, 0, 32, 32)
        self.IMAGE_FRONT_WALKING_IDLE = pygame.transform.scale(self.IMAGE_FRONT_WALKING_IDLE, (self.width, self.height))

        self.IMAGE_FRONT_WALKING_1 = self.SPRITES.get_image(32, 0, 32, 32)
        self.IMAGE_FRONT_WALKING_1 = pygame.transform.scale(self.IMAGE_FRONT_WALKING_1, (self.width, self.height))

        self.IMAGE_FRONT_WALKING_2 = self.SPRITES.get_image(0, 32, 32, 32)
        self.IMAGE_FRONT_WALKING_2 = pygame.transform.scale(self.IMAGE_FRONT_WALKING_2, (self.width, self.height))

        self.IMAGE_FRONT_ATTACK_1 = self.SPRITES.get_image(32, 32, 32, 32)
        self.IMAGE_FRONT_ATTACK_1 = pygame.transform.scale(self.IMAGE_FRONT_ATTACK_1, (self.width, self.height))

        self.IMAGE_FRONT_ATTACK_2 = self.SPRITES.get_image(0, 64, 32, 32)
        self.IMAGE_FRONT_ATTACK_2 = pygame.transform.scale(self.IMAGE_FRONT_ATTACK_2, (self.width, self.height))

        self.IMAGE_FRONT_ATTACK_3 = self.SPRITES.get_image(32, 64, 32, 32)
        self.IMAGE_FRONT_ATTACK_3 = pygame.transform.scale(self.IMAGE_FRONT_ATTACK_3, (self.width, self.height))

        self.scoreBonus = 70

    def draw(self, win, s):  # TODO dinamic
        if(self.tickTime > 60 * 6):
            self.mode = "attack"
            if(self.tickTime % 60 < 10):
                image = self.IMAGE_FRONT_ATTACK_3
            elif(self.tickTime % 30 < 15):
                image = self.IMAGE_FRONT_ATTACK_1
            elif (self.tickTime % 30 < 30):
                image = self.IMAGE_FRONT_ATTACK_2
            if(self.tickTime > 60 * 10):
                self.mode = "run"
                self.tickTime = 0
        elif(self.tickTime % 20 < 10):
            image = self.IMAGE_FRONT_WALKING_1
        elif(self.tickTime % 20 < 20):
            image = self.IMAGE_FRONT_WALKING_2


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

        #image = pygame.transform.rotate(image, angle)

        '''if(self.ori == "right"):
            image = pygame.transform.flip(image, True, False)'''

        win.blit(image, (self.x, self.y))

        for x in self.bullets:
            x.draw(win,s)

    def move(self,s):

        self.tickTime += 1
        normalTime = self.tickTime / self.clockTick
        if (normalTime % 1 == 0):
            self.attackCool += 1

        if(self.mode == "run"):

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
        if(self.mode == "run"):
            if(self.tickTime % 30 == 0):
                self.bullets.append(
                BulletMagicWarrior(self.x + self.width / 2, self.y + self.height / 2, self.player.x, self.player.y, 30, 30, 8, 1, "blue"))
                #self.tickTime = 0
        else:

            if(self.tickTime % 60 == 0):
                self.bullets.append(
                    BulletMagicWarrior2(self.x + self.width/2 - 50, self.y + self.height/2 - 50,
                                       self.player, int(s*3/80), int(s*3/80), int(s*2/80), int(s/800), "red"))
                self.bullets.append(
                    BulletMagicWarrior2(self.x + self.width/2 + 50, self.y + self.height/2 - 50,
                                       self.player, int(s*3/80), int(s*3/80), int(s*2/80), int(s/800), "red"))
                self.bullets.append(
                    BulletMagicWarrior2(self.x + self.width/2 - 50, self.y + self.height/2 + 50,
                                       self.player, int(s*3/80), int(s*3/80), int(s*2/80), int(s/800), "red"))
                self.bullets.append(
                    BulletMagicWarrior2(self.x + self.width/2 + 50, self.y + self.height/2 + 50,
                                       self.player, int(s*3/80), int(s*3/80), int(s*2/80), int(s/800), "red"))

        toRemove = []
        for b in self.bullets:
            if(self.player.confereMargem(b)):
                self.player.takeDamage(b.damage)
                toRemove.append(b)

        for b in toRemove:
            self.bullets.remove(b)


class BulletMagicWarrior(Bullet):
    def __init__(self, xo, yo, x, y, width, height, vel, damage, color):
        self.x = xo
        self.y = yo
        # self.xT = x
        # self.yT = y
        # self.m = (yo - y)/(xo - x)
        self.width = width
        self.height = height

        self.damage = damage

        self.vel = vel *2

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

        if(color == "red"):
            self.IMAGE = pygame.image.load('./sprites/tiro_2.png')
        elif(color == "blue"):
            self.IMAGE = pygame.image.load('./sprites/tiro_4.png')
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.width, self.height))
        d = degrees(asin(self.sen))

        if (auxX > 0):
            d = 180 - d
        # d -= 90

        '''if(d > 360):'''

        self.image = pygame.transform.rotate(self.IMAGE, d)

    def draw(self, win, s):
        if(self.x > 0  and self.y > 0 and self.x <= s and self.y <= s):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))

class BulletMagicWarrior2(Bullet):
    def __init__(self, xo, yo, player, width, height, vel, damage, color):
        self.x = xo
        self.y = yo
        # self.xT = x
        # self.yT = y
        # self.m = (yo - y)/(xo - x)
        self.width = width
        self.height = height

        self.player = player

        self.damage = damage

        self.vel = vel * 2

        self.cont = 0

        # self.xVel = (self.xT - self.x) / 10
        # self.yVel = (self.yT - self.y) / 10

        self.hitbox = (self.x, self.y, self.width, self.height)

        auxX = xo - self.player.x
        auxY = yo - self.player.y

        self.sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))
        self.cos = math.sqrt(1 - self.sen * self.sen)
        # print("sen:", self.sen)
        # print("cos:", self.cos)

        if (auxX < 0):
            self.xVel = self.cos * vel
        else:
            self.xVel = -self.cos * vel

        self.yVel = -self.sen * vel

        if (color == "red"):
            self.IMAGE = pygame.image.load('./sprites/tiro_2.png')
        elif (color == "blue"):
            self.IMAGE = pygame.image.load('./sprites/tiro_4.png')
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.width, self.height))
        d = degrees(asin(self.sen))

        if (auxX > 0):
            d = 180 - d
        # d -= 90

        '''if(d > 360):'''

        self.image = pygame.transform.rotate(self.IMAGE, d)

    def draw(self, win, s):
        if(self.x > 0  and self.y > 0 and self.x <= s and self.y <= s):
            #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

            win.blit(self.image, (self.x, self.y))

    def move(self):
        self.cont += 1

        if(self.cont <= 60):
            auxX = self.x - self.player.x
            auxY = self.y - self.player.y

            self.sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))
            self.cos = math.sqrt(1 - self.sen * self.sen)
            # print("sen:", self.sen)
            # print("cos:", self.cos)

            if (auxX < 0):
                self.xVel = self.cos * self.vel
            else:
                self.xVel = -self.cos * self.vel

            self.yVel = -self.sen * self.vel

            d = degrees(asin(self.sen))

            if (auxX > 0):
                d = 180 - d

            self.image = pygame.transform.rotate(self.IMAGE, d)

        if(self.cont > 60):
            self.x += self.xVel
            self.y += self.yVel
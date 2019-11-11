import pygame
from bullet import *
from gun import *
from math import asin, degrees

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width  = 64 #TODO dinamic
        self.height = 64 #TODO dinamic
        self.vel = 5 #TODO dinamic
        self.jumpForce = -15 #TODO dinamic

        self.platforms = []

        self.holdShot = False

        self.MAXLIFE = 20 #TODO dinamic
        self.life = self.MAXLIFE

        self.points = 0

        self.jumpped = False

        self.gun = Gun(20, 12, self)

        #self.g = gravity
        self.yVel = 0

        self.tickTime = 0
        self.clockTick = 60

        self.bullets = []

        self.angle = 0

        self.hitbox = (self.x, self.y, self.width, self.height)


        self.shooting = False
        self.shootCool  = 0

    def draw(self, win):

        image = 0

        if(self.shooting):
            if (self.angle >= 270 or self.angle <= 90):
                image = pygame.image.load('./sprites/cat_wizard_11.png')
            else:
                image = pygame.image.load('./sprites/cat_wizard_01.png')
            image = pygame.transform.scale(image, (self.width, self.height))

            if(self.shootCool >= 5):
                self.shooting = 0
        else:
            if(self.angle > 270 or self.angle < 90):
                image = pygame.image.load('./sprites/cat_wizard_10.png')
            else:
                image = pygame.image.load('./sprites/cat_wizard_00.png')
            image = pygame.transform.scale(image, (self.width, self.height))
            #image = pygame.transform.rotate(image, self.angle)



        win.blit(image, (self.x, self.y))

        #pygame.draw.rect(win, (124, 220, 234), (self.x, self.y, self.width, self.height))

        for x in self.bullets:
            x.draw(win)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.life) + "/" + str(self.MAXLIFE), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (60, 50)
        win.blit(text, textRect)

        text = font.render(str(self.points), True, (255, 255, 255), (0, 0, 0))
       	textRect = text.get_rect()
       	textRect.center = (400, 50)
        win.blit(text, textRect)


    def move(self, keys):
        self.tickTime += 1

        normalTime = self.tickTime / self.clockTick

        if(keys[pygame.K_a]):
            self.x -= self.vel
            for p in self.platforms:
                if(self.confereMargem(p)):
                    self.x += self.vel
                    break

        if(keys[pygame.K_d]):
            self.x += self.vel
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x -= self.vel
                    break
        if(keys[pygame.K_w]):
            self.y -= self.vel
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y += self.vel
                    break
        if(keys[pygame.K_s]):
            self.y += self.vel
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y -= self.vel
                    break

        if (keys[pygame.K_i]):
            self.holdShot = not self.holdShot
            #print(self.holdShot)

        #self.y += self.yVel

        self.hitbox = (self.x, self.y, self.width, self.height)


        btn1, btn2, btn3 = pygame.mouse.get_pressed()

        x, y = pygame.mouse.get_pos()

        xo = self.x + self.width/2
        yo = self.y + self.height/2

        auxX = xo - x
        auxY = yo - y

        sen = (auxY) / (math.sqrt(auxX * auxX + auxY * auxY))

        #if(auxY < 0):
        #sen = -sen

        self.angle = degrees(asin(sen))

        if(auxX > 0):
            self.angle = 180 - self.angle

        if(btn1 == True or self.holdShot):
            self.shootCool += 1
            if(self.shootCool >= self.gun.rateOfFire):
                self.shooting = True
                self.shootCool = 0

            self.gun.shot(self.bullets, x, y)
        else:
            self.gun.cool()
            self.shootCool += 1

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



    def damage(self, enemies):

        for e in enemies:
            toRemove = []
            for b in self.bullets:
                if(e.confereMargem(b)):
                    e.takeDamage(b.damage)
                    toRemove.append(b)
                    if(e.life <= 0):
                        self.points += 50
                    else:
                        self.points += 10
            for rm in toRemove:
                self.bullets.remove(rm)


    def confereMargem(self, *args):
        if(len(args) == 1):
            x = args[0].x
            y = args[0].y
            height = args[0].height
            width = args[0].width
        else:
            x = args[0].x
            y = args[1].y
            width = args[2].width
            height = args[3].height

        if(self.x + self.width > x and self.x < x + width):
            if(self.y + self.height > y and self.y < y + height):
                return True

        return False

    def takeDamage(self, damage):
        self.life -= damage
        self.healthCoul = 0

    def clearBullets(self):
        self.bullets = []
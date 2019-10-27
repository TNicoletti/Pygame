import pygame
from bullet import *
from gun import *

class Player(object):
    def __init__(self, x, y, platforms):
        self.x = x
        self.y = y
        self.width  = 50
        self.height = 50
        self.vel = 5
        self.jumpForce = -15

        self.platforms = platforms

        self.MAXLIFE = 400
        self.life = self.MAXLIFE

        self.points = 0

        self.jumpped = False

        self.gun = Gun(20, 1, self)

        #self.g = gravity
        self.yVel = 0

        self.tickTime = 0
        self.clockTick = 60

        self.bullets = []

        self.healthCoul = 3

        self.hitbox = (self.x, self.y, self.width, self.height)

        #self.platforms = []

    def draw(self, win):
        pygame.draw.rect(win, (124, 220, 234), (self.x, self.y, self.width, self.height))

        for x in self.bullets:
            x.draw(win)

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.life), True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (30, 15)
        win.blit(text, textRect)

        text = font.render(str(self.points), True, (255, 255, 255), (0, 0, 0))
       	textRect = text.get_rect()
       	textRect.center = (400, 15)
        win.blit(text, textRect)


    def move(self):
        self.tickTime += 1

        normalTime = self.tickTime / self.clockTick

        if(normalTime % 1 == 0):
            self.healthCoul += 1

            if(self.healthCoul >= 3):
                if (self.life < self.MAXLIFE):
                    self.life += 50

                if(self.life > self.MAXLIFE):
                    self.life = self.MAXLIFE

        keys = pygame.key.get_pressed()

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

        #self.y += self.yVel

        self.hitbox = (self.x, self.y, self.width, self.height)


        btn1, btn2, btn3 = pygame.mouse.get_pressed()

        if(btn1 == True):
            x, y = pygame.mouse.get_pos()

            self.gun.shot(self.bullets, x, y)
        else:
        	self.gun.cool()

        for x in self.bullets:
            x.move()

        toRemove = []

        for x in self.bullets:
            if(x.x < 0 or x.x > 500 or x.y < 0 or x.y > 500):
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
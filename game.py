import pygame
from player import *
from enemy import *
from platform import *
from bullet import *
from shop import *
from gun import *

import random

pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("GUEIME")

x = 50
y = 50
width  = 40
height = 60
vel = 5

gravity = .8

run = True

player    = Player(0, 0, gravity)
enemies   = []
platforms = [Platform(-1, 0, 1, 500),
			 Platform(0, 490, 2000, 20),
			 Platform(0, 400, 100, 20),
			 Platform(400, 450, 100, 50),
			 Platform(300, 450, 50, 50),
			 Platform(400, 350, 200, 20),
			 Platform(400, 250, 100, 20),
			 Platform(400, 150, 100, 20),
			 Platform(725, 300, 150, 20),
			 Platform(950, 200, 100, 20)]

shops = [Shop(0, 420, Gun(50, 2, player), 4000, player),
Shop(500, 420, Gun(1500, 1 * 60, player), 5000, player),
Shop(1000, 130, Gun(33000, 2 * 60, player), 20000, player)]

tickTime = 0
normalTime = 0
clockTick = 60
cont = 0

tela = [0 , 0]

while(run):
	tickTime += 1
	normalTime = tickTime/clockTick
	clock.tick(clockTick)

	if(normalTime % 1 == 0):
		cont+= 1

		if(cont == 3):
			cont = 0

			rand = random.randint(0, 2)

			if(rand == 0):
				enemies.append(Enemy(250 - 500 * tela[0], 250, player, gravity))
			elif(rand == 1):
				enemies.append(Enemy(1000 - 500 * tela[0], 400, player, gravity))
			elif(rand == 2):
				enemies.append(Enemy(1500 - 500 * tela[0], 400, player, gravity))
	
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	win.fill((0, 0, 0))

	for s in shops:
		s.draw(win)

	player.commitLandded(platforms)
	player.move()
	player.draw(win)
	player.damage(enemies)
	#print(player.y)

	toRemove = []

	keys = pygame.key.get_pressed()

	if(keys[pygame.K_f]):
		for s in shops:
			s.buy()
	for e in enemies:
		if (e.life <= 0):
			toRemove.append(e)
			continue

		e.commitLandded(platforms)
		e.move()
		e.draw(win)
		e.do_attack()

	for rm in toRemove:
		enemies.remove(rm)

	for p in platforms:
		p.move()
		p.draw(win)

	if(player.x > 500):
		for e in enemies:
			e.x -= 500

		for p in platforms:
			p.x -= 500

		for s in shops:
			s.x -= 500

		player.x -= 500

		tela[0] += 1

	if(player.x < -player.width):
		for e in enemies:
			e.x += 500

		for p in platforms:
			p.x += 500

		for s in shops:
			s.x += 500

		player.x += 500

		tela[0] -= 1
	
	#pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.flip()

#pygame.display.flip()
pygame.quit()
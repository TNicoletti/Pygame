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

width = 800
height = 800

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("GAYME")

x = 50
y = 50
vel = 5

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#gravity = .8

run = True

platforms = [Platform(0, 0, 1, 800),
			 Platform(0, 800, 800, 1),
			 Platform(0, 0, 800, 1),
			 Platform(799, 0, 0, 800)]

player    = Player(250, 250, platforms)
enemies   = []

shops = [Shop(0, 420, Gun(50, 2, player), 0, player),
Shop(500, 420, Gun(1500, 5 * 60, player), 3000, player),
Shop(1000, 130, Gun(33000, 2 * 60, player), 5000, player)]

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
				enemies.append(Enemy(250 - width * tela[0], 250 - height * tela[0], player, platforms))
			elif(rand == 1):
				enemies.append(Enemy(1000 - width * tela[0], 400 - height * tela[0], player, platforms))
			elif(rand == 2):
				enemies.append(Enemy(1500 - width * tela[0], 400 - height * tela[0], player, platforms))
				enemies.append(Enemy(1500 - width * tela[0], 400 - height * tela[0], player, platforms))

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	win.fill((0, 0, 0))

	for s in shops:
		s.draw(win)

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

		e.move()
		e.draw(win)
		e.do_attack()

	for rm in toRemove:
		enemies.remove(rm)

	for p in platforms:
		p.move()
		p.draw(win)

	if(player.x > width):
		for e in enemies:
			e.x -= width

		for p in platforms:
			p.x -= width

		for s in shops:
			s.x -= width

		player.x -= width

		tela[0] += 1

	if(player.x < -player.width):
		for e in enemies:
			e.x += width

		for p in platforms:
			p.x += width

		for s in shops:
			s.x += width

		player.x += width

		tela[0] -= 1

	if (player.y > height):
		for e in enemies:
			e.y -= height

		for p in platforms:
			p.y -= height

		for s in shops:
			s.y -= height

		player.y -= height

		tela[1] += 1

	if (player.y < -player.height):
		for e in enemies:
			e.y += height

		for p in platforms:
			p.y += height

		for s in shops:
			s.y += height

		player.y += height

		tela[1] -= 1
	
	#pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	pygame.display.flip()

#pygame.display.flip()
pygame.quit()
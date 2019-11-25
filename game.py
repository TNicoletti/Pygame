#!/usr/bin/python

import pygame
import random
import string
from player import *
from enemy import *
from platform import *
from bullet import *
from shop import *
from gun import *
from levelGenerator import *
from Door import *
from patocomarma import *
from patocomarmaebandana import *
from MagicWarrior1 import *

import random
#print(string.ascii_lowercase[0:16])
seed = ''.join(random.choice(string.ascii_lowercase[0:16]) for i in range(10))
#seed = "abcdefghij"
#print(seed)

width = 800
height = 800

x = 50
y = 50
vel = 5

pygame.init()

clock = pygame.time.Clock()


win = pygame.display.set_mode((width, height))

pygame.display.set_caption("GAYME")

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#gravity = .8

run = True

obstaculo = []

player    = Player(250, 250)
enemies   = []

shops = []

clockTick = 60

andar = 0

lg = levelGenerator(player,seed,10)
enemies = lg.getAtualMap().enemies
obstaculo = lg.getAtualMap().obstaculos
player.platforms = obstaculo
shops = lg.getAtualMap().shops

doors = [Door(300, 0, 100, 10, "left"), Door(400, 0, 100, 10, "right"),
		 Door(300, 790, 100, 10, "left"), Door(400, 790, 100, 10, "right"),
		 Door(0, 300, 10, 100, "up"), Door(0, 400, 10, 100, "down"),
		 Door(790, 300, 10, 100, "up"), Door(790, 400, 10, 100, "down")]
player.doors = doors

def changeSlice(nmap):
	global enemies
	global obstaculo
	global player
	global shops
	global doors
	enemies = nmap.enemies
	obstaculo = nmap.obstaculos
	player.platforms = obstaculo
	player.items = []
	shops = nmap.shops
	putDoors()
	player.doors = doors

def putDoors():
	global doors
	global lg
	global enemies
	doors = []

	if(not len(enemies) == 0):
		if(lg.map[lg.tela[0] - 1][lg.tela[1]] != 0):
			doors.append(Door(300, 0, 100, 10, "left"))
			doors.append(Door(400, 0, 100, 10, "right"))

		if((lg.map[lg.tela[0] + 1][lg.tela[1] + 1] != 0)):
			doors.append(Door(300, 790, 100, 10, "left"))
			doors.append(Door(400, 790, 100, 10, "right"))

		if ((lg.map[lg.tela[0]][lg.tela[1] - 1] != 0)):
			doors.append(Door(0, 300, 10, 100, "up"))
			doors.append(Door(0, 400, 10, 100, "down"))

		if ((lg.map[lg.tela[0]][lg.tela[1] + 1] != 0)):
			doors.append(Door(790, 300, 10, 100, "up"))
			doors.append(Door(790, 400, 10, 100, "down"))

lg.map[25][25].visto = 1
#lg.map[25][25].tipo = 3
#lg.marcarVisto()
bg = (122, 48, 72)
#enemies.append(MagicWarrior1(10, 10, player, obstaculo))
#enemies.append(MagicWarrior1(790 - 75, 10, player, obstaculo))
#enemies.append(Patocomarma(10, 10, player, obstaculo))
#enemies.append(Patocomarmaebandana(10, 10, player, obstaculo))
#enemies.append(TheFirstBoss(400 - 50, 400 - 50, player, obstaculo))

while(run):
	clock.tick(clockTick)

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	keys = pygame.key.get_pressed()

	if(keys[pygame.K_ESCAPE] or player.life<=0):
		run = False

	win.fill(bg)

	for s in shops:
		s.draw(win)

	for p in obstaculo:
		p.move()
		p.draw(win)

	player.move(keys)
	player.draw(win)
	player.damage(enemies)

	toRemove = []

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

	if (len(enemies) == 0):
		if(lg.getAtualMap().tipo==3):
			andar +=1

			seed = ''.join(random.choice(string.ascii_lowercase[0:16]) for i in range(10))

			lg = levelGenerator(player,seed,10+(andar*2))
			enemies = lg.getAtualMap().enemies
			obstaculo = lg.getAtualMap().obstaculos
			player.platforms = obstaculo
			shops = lg.getAtualMap().shops

			bg = ((ord(seed[0])-ord('a'))*17,(ord(seed[1])-ord('a'))*17,(ord(seed[2])-ord('a'))*17)

			player.life = player.MAXLIFE

		for p in doors:
			p.move()
		lg.marcarVisto()

	for p in doors:
		p.draw(win)

	for i in player.items:
		i.draw(win)
		if(i.confereMargem(player)):
			i.get(player)

	correction = 10

	if(player.x > width):
		player.x -= width - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("r"))

	if(player.x < -player.width):
		player.x += width  - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("l"))


	if (player.y > height):
		player.y -= height - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("d"))

	if (player.y < -player.height):
		player.y += height - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("u"))

	for i in range(len(lg.map)):
		for j in range(len(lg.map[i])):
			if lg.map[i][j] != None:
				if i == lg.tela[0] and j == lg.tela[1]:
					pygame.draw.rect(win, (150, 0, 0), (width-50*5+5*j, height-50*5+5*i, 4, 4))
				elif lg.map[i][j].visto == 1:
					if(lg.map[i][j].tipo == 2):
						pygame.draw.rect(win, (0, 0, 150), (width-50*5+5*j, height-50*5+5*i, 4, 4))
					elif(lg.map[i][j].tipo == 3):
						pygame.draw.rect(win, (255, 150, 0), (width-50*5+5*j, height-50*5+5*i, 4, 4))
					else:
						pygame.draw.rect(win, (0, 150, 0), (width-50*5+5*j, height-50*5+5*i, 4, 4))
				elif lg.map[i][j].visto == 2:
					pygame.draw.rect(win, (50, 50, 50), (width-50*5+5*j, height-50*5+5*i, 4, 4))
	pygame.display.flip()

pygame.quit()
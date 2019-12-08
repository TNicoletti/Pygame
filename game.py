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

size = 800

x = int(size/16) #50
y = int(size/16) #50
vel = int(size/160) #5

pygame.init()

clock = pygame.time.Clock()


win = pygame.display.set_mode((size, size))

pygame.display.set_caption("GAYME")

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

#gravity = .8

run = True

obstaculo = []

player    = Player(size/4, size/4, size)
enemies   = []

shops = []

clockTick = 60

andar = 0

lg = levelGenerator(player,seed,10,size)
enemies = lg.getAtualMap().enemies
obstaculo = lg.getAtualMap().obstaculos
player.platforms = obstaculo
shops = lg.getAtualMap().shops

doors = [Door(int(size*3/8), 0, int(size/8), int(size/80), "left"), Door(int(size*4/8), 0, int(size/8), int(size/80), "right"),
		 Door(int(size*3/8), int(size-size/80), int(size/8), int(size/80), "left"), Door(int(size*4/8), int(size-size/80), int(size/8), int(size/80), "right"),
		 Door(0, int(size*3/8), int(size/80), int(size/8), "up"), Door(0, int(size*4/8), 10, int(size/8), "down"),
		 Door(int(size-size/80), int(size*3/8), int(size/80), int(size/8), "up"), Door(int(size-size/80), int(size*4/8), 10, int(size/8), "down")]
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
			doors.append(Door(int(size*3/8), 0, int(size/8), int(size/80), "left"))
			doors.append(Door(int(size*4/8), 0, int(size/8), int(size/80), "right"))

		if((lg.map[lg.tela[0] + 1][lg.tela[1] + 1] != 0)):
			doors.append(Door(int(size*3/8), int(size-size/80), int(size/8), int(size/80), "left"))
			doors.append(Door(int(size*4/8), int(size-size/80), int(size/8), int(size/80), "right"))

		if ((lg.map[lg.tela[0]][lg.tela[1] - 1] != 0)):
			doors.append(Door(0, int(size*3/8), int(size/80), int(size/8), "up"))
			doors.append(Door(0, int(size*4/8), int(size/80), int(size/8), "down"))

		if ((lg.map[lg.tela[0]][lg.tela[1] + 1] != 0)):
			doors.append(Door(int(size-size/80), int(size*3/8), int(size/80), int(size/8), "up"))
			doors.append(Door(int(size-size/80), int(size*4/8), int(size/80), int(size/8), "down"))

lg.map[25][25].visto = 1
#lg.map[25][25].tipo = 3
#lg.marcarVisto()
bg = (122, 48, 72)
#enemies.append(MagicWarrior1(10, 10, player, obstaculo))
#enemies.append(MagicWarrior1(790 - 75, 10, player, obstaculo))
#enemies.append(Patocomarma(10, 10, player, obstaculo))
enemies.append(Patocomarmaebandana(10, 10, player, obstaculo, size))
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

	player.move(keys,size)
	player.draw(win,size)
	player.damage(enemies,size)

	toRemove = []

	if(keys[pygame.K_f]):
		for s in shops:
			s.buy()

	for e in enemies:
		if (e.life <= 0):
			toRemove.append(e)
			continue

		e.move(size)
		e.draw(win,size)
		e.do_attack(size)

	for rm in toRemove:
		enemies.remove(rm)

	if (len(enemies) == 0):
		if(lg.getAtualMap().tipo==3):
			andar +=1

			seed = ''.join(random.choice(string.ascii_lowercase[0:16]) for i in range(10))

			lg = levelGenerator(player,seed,10+(andar*2),size)
			enemies = lg.getAtualMap().enemies
			obstaculo = lg.getAtualMap().obstaculos
			player.platforms = obstaculo
			shops = lg.getAtualMap().shops

			bg = ((ord(seed[0])-ord('a'))*17,(ord(seed[1])-ord('a'))*17,(ord(seed[2])-ord('a'))*17)

			player.life = player.MAXLIFE

		for p in doors:
			p.move(size)
		lg.marcarVisto()

	for p in doors:
		p.draw(win)

	for i in player.items:
		i.draw(win,size)
		if(i.confereMargem(player)):
			i.get(player)

	correction = size*10/800 

	if(player.x > size):
		player.x -= size - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("r"))

	if(player.x < -player.width):
		player.x += size  - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("l"))


	if (player.y > size):
		player.y -= size - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("d"))

	if (player.y < -player.height):
		player.y += size - correction
		player.clearBullets()
		changeSlice(lg.changeSlice("u"))

	for i in range(len(lg.map)):
		for j in range(len(lg.map[i])):
			if lg.map[i][j] != None:
				if i == lg.tela[0] and j == lg.tela[1]:
					pygame.draw.rect(win, (150, 0, 0), (size-size*5/16+5*j, size-size/16*5+5*i, size/200, size/200))
				elif lg.map[i][j].visto == 1:
					if(lg.map[i][j].tipo == 2):
						pygame.draw.rect(win, (0, 0, 150), (size-size*5/16+5*j, size-size/16*5+5*i, size/200, size/200))
					elif(lg.map[i][j].tipo == 3):
						pygame.draw.rect(win, (255, 150, 0), (size-size*5/16+5*j, size-size/16*5+5*i, size/200, size/200))
					else:
						pygame.draw.rect(win, (0, 150, 0), (size-size*5/16+5*j, size-size/16*5+5*i, size/200, size/200))
				elif lg.map[i][j].visto == 2:
					pygame.draw.rect(win, (50, 50, 50), (size-size*5/16+5*j, size-size/16*5+5*i, size/200, size/200))
	pygame.display.flip()

pygame.quit()
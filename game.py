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

import random

seed = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
print(seed)

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

lg = levelGenerator(player)
enemies = lg.getAtualMap().enemies
obstaculo = lg.getAtualMap().obstaculos
player.platforms = obstaculo
shops = lg.getAtualMap().shops

def changeSlice(nmap):
	global enemies
	global obstaculo
	global player
	global shops
	enemies = nmap.enemies
	obstaculo = nmap.obstaculos
	player.platforms = obstaculo
	shops = nmap.shops

while(run):
	clock.tick(clockTick)

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	keys = pygame.key.get_pressed()

	if(keys[pygame.K_ESCAPE]):
		run = False

	win.fill((0, 0, 0))

	for s in shops:
		s.draw(win)

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

	'''if (len(enemies) == 0):
		doors.move()'''

	for p in obstaculo:
		p.move()
		p.draw(win)

	if(player.x > width):
		player.x -= width
		player.clearBullets()
		changeSlice(lg.changeSlice("r"))

	if(player.x < -player.width):
		player.x += width
		player.clearBullets()
		changeSlice(lg.changeSlice("l"))


	if (player.y > height):
		player.y -= height
		player.clearBullets()
		changeSlice(lg.changeSlice("d"))

	if (player.y < -player.height):
		player.y += height
		player.clearBullets()
		changeSlice(lg.changeSlice("u"))

	pygame.display.flip()

pygame.quit()
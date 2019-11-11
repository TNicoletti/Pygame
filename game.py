#!/usr/bin/python

import pygame
from player import *
from enemy import *
from platform import *
from bullet import *
from shop import *
from gun import *
from levelGenerator import *
from Door import *

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

while(run):
	clock.tick(clockTick)

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False

	win.fill((0, 0, 0))

	for s in shops:
		s.draw(win)

	player.move()
	player.draw(win)
	player.damage(enemies)

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

	if (len(enemies) == 0):
		for p in doors:
			p.move()

	for p in obstaculo:
		p.move()
		p.draw(win)

	for p in doors:
		p.draw(win)

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

	pygame.display.flip()

pygame.quit()
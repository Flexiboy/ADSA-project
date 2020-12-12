#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

import time

class Vent:
	
	def __init__(self, room1, room2, traveltime = 0):
		"""
		Init of a vent
		:param self: the vent itself
		:param room1: the room 1 connected to room 2
		:param room2: the room 2 connected to room 1
		:param traveltime: the time to travel the vent
		"""
		self.room1 = room1
		self.room2 = room2
		self.traveltime = traveltime

	def use(self, player):
		"""
		Impostor using a vent
		:param player: the player using the vent
		"""
		if player.role == impostor:
			time.sleep(self.traveltime)
			if player.location == self.room1:
				player.location = self.room2
			else:
				player.location = self.room1

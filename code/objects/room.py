#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

class Room:
	
	def __init__(self, name, form, connected):
		"""
		Init of a room
		"""
		self.name = name
		self.form = form
		# The model of the form will be a matrix with different values in it:
		# 0, this is void
		# 1, this is a block without any specification
		# 2, this is a block with a task
		# 3, this is a sabotage location
		# 4, this is a vent location
		# -1, this is a door location
		self.connected = connected # the rooms that are connected to this one

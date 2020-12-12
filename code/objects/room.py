#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.vent import *
from objects.task import *
from objects.sabotage import *

class Room:
	
	oef __init__(self, name, form, connected_rooms, connected_corr, vents, tasks, sabotage):
		"""
		Init of a room
		"""
		self.name = name
		self.form = form
		# The model of the form will be a matrix with different values in it:
		# 0, this is void
		# 1, this is a block without any specification
		# -1, this is a door location
		self.connected_rooms = connected # the rooms that are connected to this one
		self.connected_corr = connected_corr
		self.vents = vents
		self.tasks = tasks
		self.sabotage = sabotage

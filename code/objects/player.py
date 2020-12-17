#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""

Class Player

"""

class Player:
	def __init__(self, _id, name):
		"""
		Initialize the player
		:param self: the player itself
		:param _id: player id
		:param name: the player name
		"""
		self._id = _id
		self.name = name
		self.rank = 0
		self.score = 0
		self.role = ""
		self.Score_games = []
		self.Score_turns = []

	def __str__(self):
		"""
		Description of the player
		:param self: the player itself
		:return: player's description
		"""
		return ('Player name: ' + str(self.name) 
            + ' Current rank: ' + str(self.rank)
            + ' Current score: '+ str(self.score))

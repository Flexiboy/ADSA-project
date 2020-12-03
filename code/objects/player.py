#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN
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

	def __str__(self):
		"""
		Description of the player
		:param self: the player itself
		:return: player's description
		"""
		return ('Player name: ' + str(self.name) 
            + ' Current rank: ' + str(self.rank)
            + ' Current score: '+ str(self.score))
	
	def __getitem__(self, index):
		if(index == "role"):
			value = self.role
		if(index == "name"):
			value = self.name
		if(index == "id"):
			value = self._id
		return value
	def __setitem__(self, index, value):
		if(index == "role"):
			self.role = value

	def ScoreAdd(self, action):
		score_game = 0
		if(self.role == "impostor"):
			if(action== "kill"):
				score_game += 1
			if(action== "undiscovered_murder"):
				score_game += 3
			if (action == "win"):
				score_game += 10
		if (self.role == "crewmate"):
			if (action == "unmask_impostor"):
				score_game += 3
			if (action == "task_done"):
				score_game += 1
			if (action == "win"):
				score_game += 5
		self.Score_games.append(score_game)

	def ScoreUpdate(self):
		count = len(self.Score_games)
		while(True):
			self.score += self.Score_games.pop()
			if (len(self.Score_games) == 0):
				break
		self.score /= count

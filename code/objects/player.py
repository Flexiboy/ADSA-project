#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""

Class Player

"""

class Player:
	def __init__(self, _id, name, location):
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
		self.location = location

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
		if(index == "score_games"):
			value = self.Score_games
		if(index == 'location'):
			value = self.location
		return value
		
	def __setitem__(self, index, value):
		if(index == "role"):
			self.role = value
		if(index == 'location'):
			self.location = value

	"""
	called during a game

	add the score in Score turns
	"""
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
		self.Score_turns.append(score_game)

	"""
	called at the end of a game

	reset the Score_turns list and add the final score to 
	the Score games list
	"""
	def Score_game(self):
		score_game = 0
		for score in self.Score_turns:
			score_game += score
		self.Score_turns = []
		self.Score_games.append(score_game)
		
	"""
	called for each elimination phase of the tournament.

	Addition of all score of Score games list, reset it and
	set the player score by the addition / number of games (Score games list length) 

	"""
	def ScoreUpdate(self):
		count = len(self.Score_games)
		while(True):
			self.score += self.Score_games.pop()
			if (len(self.Score_games) == 0):
				break
		self.score /= count

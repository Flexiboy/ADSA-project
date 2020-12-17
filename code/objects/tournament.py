#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.game import *

class Tournament:

	def __init__(self, numberOfPlayers):
		self.player_list = self.setup(numberOfPlayers)
		self.tournament = []
		self.game_list = []
		self.alive = []
		self.eliminated = []

		for player in self.player_list:
			self.alive.append(player)

		while(len(self.alive) > 10):
			for i in range(3):
				self.game_list = self.newRound()
				self.tournament.append(self.game_list)
				self.game_list = []
			self.updateRank()
			self.ejectPlayers()

		for i in range(5):
			self.game_list = self.newRound()
			self.tournament.append(self.game_list)
			self.game_list = []
	
		self.updateRank()
		self.showTop10()

	def setup(self, numberOfPlayers):
		"""
		Setting up the tournament with the 100 player
		:return: the player list
		"""
		player_list = []
		player_name = ""
		for i in range(numberOfPlayers):
			#player_name = input("Enter player name > ")
			player_name = f'player{i}'
			new_player = Player(i, player_name)
			player_list.append(new_player)
			del new_player
		return player_list

	def newRound(self):
		"""
		Setting up a new round
		:param alive: the remaining players in the tournament
		:return: the list of the game
		"""
		game_list = []
		player_list = []
		player_number = 0

		self.updateRank()

		for i in range(0, len(self.alive), 10):
			for j in range(10): #Selecting the players of the game
				player_list.append(self.alive[i + j])
			new_game = Game(self.player_list)
			new_game.RndScores()
			game_list.append(new_game)
			del new_game
			player_list = []

		return game_list

	def updateRank(self):
		"""
		Updates the rank of the players
		"""
		rank = 0
		self.alive = sorted(self.alive, key=lambda player: player.score, reverse = True)
		for player in self.alive:
			rank += 1
			player.rank = rank

	def ejectPlayers(self):
		"""
		Ejects the players that are too low ranked
		"""
		self.alive = sorted(self.alive, key=lambda player: player.rank, reverse = True)
		for i in range(10):
			self.eliminated.append(self.alive[0])
			self.alive.pop(0)

	def showLeaderboard(self):
		"""
		Shows the Leaderboard
		"""
		sorted(self.player_list, key=lambda player: player.rank, reverse = False)
		for player in self.player_list:
			print(player)

	def showTop10(self):
		"""
		Shows the TOP 10 players
		"""
		self.updateRank()
		print('')
		for i  in range(10):
			if i == 3:
				print('')
			print(f'{i + 1}. {self.alive[i]}')
		print('')

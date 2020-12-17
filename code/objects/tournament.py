#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.game import *

class Tournament:

	def __init__(self, numberOfPlayers):
		"""
		Initialize the tournament (step 1)
		:param self: the tournament itself
		:param numberOfPlayers: the number of players in the tournament
		
		This initialization method runs the whole tournament and shows the top 10
		players at the end of the game
		"""
		self.player_list = self.setup(numberOfPlayers) #Creates the player in the tournament
		self.tournament = []
		self.game_list = []
		self.alive = []
		self.eliminated = []

		for player in self.player_list:
			self.alive.append(player)

		# The firsts rounds, there is 3 game then we remove the last
		# 10 players and we do it until there remains 10 players
		while(len(self.alive) > 10):
			for i in range(3):
				self.game_list = self.newRound()
				self.tournament.append(self.game_list)
				self.game_list = []
			self.updateRank()
			self.ejectPlayers()

		# The final rounds, there is 5 games and then the tournament
		# is finished
		for i in range(5):
			self.game_list = self.newRound()
			self.tournament.append(self.game_list)
			self.game_list = []
	
		self.updateRank()
		self.showTop10()



	def setup(self, numberOfPlayers):
		"""
		Creates all the players and set the tournament up
		:param self: the tournament itself
		:param nuumberOfPlayers: the number of players that has to be created
		:return: the player list
		"""
		player_list = []
		player_name = ""
		for i in range(numberOfPlayers):
			player_name = f'player{i + 1}' #Creates the player name with this format: player1, player2, ...
			new_player = Player(i, player_name)
			player_list.append(new_player)
			del new_player
		return player_list



	def newRound(self):
		"""
		Setting up a new round
		:param self: the tournament itself
		:return: the list of the game
		"""
		game_list = []
		player_list = []
		player_number = 0

		self.updateRank() #Updates the rank in order to better select players in the game

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
		:param self: the tournament itself
		"""
		rank = 0
		# This function returns a sorted array by player score, descending
		self.alive = sorted(self.alive, key=lambda player: player.score, reverse = True)
		for player in self.alive:
			rank += 1
			player.rank = rank



	def ejectPlayers(self):
		"""
		Ejects the players that are too low ranked
		:param self: the tournament itself
		"""
		# This functions returns a sorted array by player rank, descending
		self.alive = sorted(self.alive, key=lambda player: player.rank, reverse = True)
		# This block removes the first 10 players in the sorted list alive
		for i in range(10):
			self.eliminated.append(self.alive[0])
			self.alive.pop(0)



	def showLeaderboard(self):
		"""
		Shows the Leaderboard
		:param self: the tournament itself
		"""
		sorted(self.player_list, key=lambda player: player.rank, reverse = False)
		for player in self.player_list:
			print(player)



	def showTop10(self):
		"""
		Shows the TOP 10 players
		:param self: the tournament itself
		"""
		self.updateRank()
		print('')
		for i  in range(10):
			if i == 3:
				print('')
			print(f'{i + 1}. {self.alive[i]}')
		print('')

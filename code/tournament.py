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

		for player in player_list:
			self.alive.append(player)

		while(len(alive) > 10):
			for i in range(3):
				game_list = newRound()
				tournament.append(game_list)
				game_list = []
			updateRank()
			ejectPlayers()
	
		for i in range(5):
			game_list = newRound(alive)
			tounrament.append(game_list)
			game_list = []
	
		updateRank()

	def setup(self, numberOfPlayers):
		"""
		Setting up the tournament with the 100 player
		:return: the player list
		"""
		player_list = []
		player_name = ""
		for i in range(numberOfPlayers):
			player_name = input("Enter player name > ")
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

		updateRank()

		for i in range(len(self.alive) / 10):
			for j in range(10): #Selecting the players of the game
				player_list.append(self.alive[i * 10 + j])
			new_game = Game(self.player_list)
			game_list.append(new_game)
			del new_game
			player_list = []

		return game_list

	def updateRank(self):
		"""
		Updates the rank of the players
		"""
		rank = 0
		sorted(self.alive, key=lambda player: player['score'], reverse = True)
		for player in self.alive:
			rank += 1
			player['rank'] = rank

	def ejectPlayers(self):
		"""
		Ejects the players that are too low ranked
		"""
		sorted(self.alive, key=lambda player: player['rank'], reverse = True)
		for i in range(10):
		self.eliminated.append(alive[0])
		self.alive.pop(0)

	def showLeaderboard():
		"""
		Shows the Leaderboard
		"""
		sorted(self.player_list, key=lambda player: player['rank'], reverse = False)
		for player in self.player_list:
			print(player)

	def showTop10():
		"""
		Shows the TOP 10 players
		"""
		updateRank()
		for i  in range(10):
			print(f'{i}. {self.alive[i]}')

def main():
	"""
	The main
	"""

if __name__ == '__main__':
	main()

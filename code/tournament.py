#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

import random as rnd

from objects.game import *
from objects.player import *

def setUp():
	"""
	Setting up the tournament with the 100 player
	:return: the player list
	"""
	player_list = []
	player_name = ""
	for i in range(100):
		player_name = input("Enter player name > ")
		new_player = Player(i, player_name)
		player_list.append(new_player)
		del new_player
	return player_list

def new_round(alive):
	"""
	Setting up a new round
	:param alive: the remaining players in the tournament
	:return: the list of the game
	"""
	game_list = []
	alive_temp = []
	player_list = []
	player_number = 0

	#Setting a temporary list to  avoid compromising alive list's data
	for player in alive:
		alive_temp.append(player)

	for i in range(len(alive) / 10):
		for j in range(10): #Selecting the players of the game
			player_number = rnd.randrange(0, len(alive_temp), 1)
			player_list.append(alive_temp[player_number])
			alive_temp.pop(player_number)
		new_game = Game(player_list)
		game_list.append(new_game)
		del new_game
		player_list = []

	return game_list

def updateRank(alive):
	"""
	Updates the rank of the players
	:param alive: the remaining players in the tournament
	"""
	rank = 0
	sorted(alive, key=lambda player: player['score'])
	for player in alive:
		rank += 1
		player['rank'] = rank

def main():
	player_list = setUp()

if __name__ == '__main__':
	main()

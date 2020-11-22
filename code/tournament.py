#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.game import *

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

def newRound(alive):
	"""
	Setting up a new round
	:param alive: the remaining players in the tournament
	:return: the list of the game
	"""
	game_list = []
	player_list = []
	player_number = 0

	updateRank(alive)

	for i in range(len(alive) / 10):
		for j in range(10): #Selecting the players of the game
			player_list.append(alive[i * 10 + j])
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
	sorted(alive, key=lambda player: player['score'], reverse = True)
	for player in alive:
		rank += 1
		player['rank'] = rank

def ejectPlayers(alive, eliminated):
	"""
	Ejects the players that are too low ranked
	:param alive: the alive players
	:param eliminated: the eliminated players
	"""
	sorted(alive, key=lambda player: player['rank'], reverse = True)
	for i in range(10):
		eliminated.append(alive[0])
		alive.pop(0)

def main():
	"""
	The main
	"""
	player_list = setUp()
	tournament = []
	game_list = []
	alive = []
	eliminated = []

	for player in player_list:
		alive.append(player)

	while(len(alive) > 10):
		for i in range(3):
			game_list = newRound(alive)
			tournament.append(game_list)
			game_list = []
		updateRank(alive)
		ejectPlayers(alive, eliminated)
	
	for i in range(5):
		game_list = newRound(alive)
		tounrament.append(game_list)
		game_list = []
	
	updateRank(alive)

if __name__ == '__main__':
	main()

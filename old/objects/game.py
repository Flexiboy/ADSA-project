#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""

Class game

"""

import random

from objects.player import *

class Game:

	def __init__(self, player_list):
		"""
		Game init
		:param player_list: player list in the game
		"""
		self.impostors = []
		self.crewmates = []
		self.player_list = player_list
		self.alive = []

		random.shuffle(player_list) # shuffling the list to select randomize impostors

		# Delink alive and list_player
		for player in self.player_list:
			self.alive.append(player)

		impostor_count = 2

		# Loop that places random player in list of crew or impostor and set their role
		if impostor_count > 0:
			impostor_count -= 1
			player.role = 'impostor'
			self.impostors.append(player)
		else:
			player.role = 'crewmate'
			self.crewmates.append(player)



	def __str__(self):
		"""
		Stringify the game object
		:param self: the game itself
		:return: increased verbosity of object game
		"""
		return ('The game have:\n2 impostors: ' +  self.Str_list_name(self.impostors) 
			+ '\n8 crewmates: ' + self.Str_list_name(self.crewmates))



	def Couple_probable_impostors_Bellman(self):
		"""
		Method to find probable impostors in a graph with bellman_ford
		:param self: the game itself
		return: list of impostor's couple
		"""
		graph = {'0': {'1': 1, '4': 1, '5': 1},
			 '1': {'0': 1, '2': 1, '6': 1},
			 '2': {'1': 1, '3': 1, '7': 1},
			 '3': {'2': 1, '4': 1, '8': 1},
			 '4': {'0': 1, '3': 1, '9': 1},
			 '5': {'0': 1, '7': 1, '8': 1},
			 '6': {'1': 1, '8': 1, '9': 1},
			 '7': {'2': 1, '5': 1, '9': 1},
			 '8': {'3': 1, '5': 1, '6': 1},
			 '9': {'4': 1, '6': 1, '7': 1}}   
                    
		probable_impostors = []
		# Store all distance from the three first probable impostor
		distance_1 = self.bellman_ford(graph, '1')   
		distance_4 = self.bellman_ford(graph, '4')  
		distance_5 = self.bellman_ford(graph, '5')

		# For each list, we check a second probable impostor and create a couple with it and the first
		for player in distance_1:
			# If the player is not another first probable impostor
			if(player != "5" and player != "4"):
				# If the cost is higher than two, not the dead or a seen player (the first pobable impostor)
				if(distance_1[player] > 1):
					# We add the couple to the list
					probable_impostors.append(["1", player])

		for player in distance_4:
			if(player != "1" and player != "5"):
				if(distance_4[player] > 1):
					probable_impostors.append(["4", player])

		for player in distance_5:
			if(player != "1" and player != "4"):
				if(distance_5[player] > 1):
					probable_impostors.append(["5", player])
        
		return probable_impostors



	def bellman_ford(self, graph, source):
		"""
		Bellman Ford algorithm
		:param self: the map itself
		:param graph: the graph with nodes and vertices
		:param source: the node from which we look all path to other nodes
		:return: dictionnary of all node from the source node with the distance from it 
		"""
		# Step 1: Prepare the distance and predecessor for each node
		distance, predecessor = dict(), dict()

		#for each node
		for node in graph:
			#set the distance to infinite
			distance[node], predecessor[node] = float('inf'), None
		#the distance for the node that we look is 0. it's the start point
		distance[source] = 0

		# Step 2: Relax the edges
		for _ in range(len(graph) - 1):
			for node in graph:
				for neighbour in graph[node]:
					# If the distance between the node and the neighbour is lower than the current, store it
					if distance[neighbour] > distance[node] + graph[node][neighbour]:
						distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

		#retrun a dictionnary with all distance
		return distance



	def RndScores(self, nGames):
		"""
		Generates random scores
		:param self: the map itself
		:param nGames: number of games played
		"""
		for player in self.player_list:
			player.score = ((nGames - 1) / nGames * player.score) + (1 / nGames * random.randrange(0, 12, 1))

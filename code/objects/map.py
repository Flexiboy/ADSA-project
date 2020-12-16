#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

#from objects.room import *
#from objects.player import *

"""

Class Map

"""

class Map:

	def __init__(self, paths):
		"""
		Initialize the map
		:param self: the map itself
		:param path: the path to the files containing init infos
		"""
		
		self.map = {
			'cafeteria': {'weapons', 'upper e', 'medbay', 'admin', 'storage'},
			'weapons': {'cafeteria', 'o2', 'navigations', 'shield'},
			'navigations': {'o2', 'weapons', 'shield'},
			'o2': {'weapons', 'navigations', 'shield'},
			'shield': {'weapons', 'o2', 'navigations', 'communication', 'storage'},
			'communication': {'shield', 'storage'},
			'storage': {'communication', 'shield', 'admin', 'cafeteria', 'electrical', 'lower e'},
			'electrical': {'storage', 'lower e'},
			'lower e': {'storage', 'electrical', 'security', 'reactor', 'upper e'},
			'reactor': {'security', 'upper e', 'lower e'},
			'upper e': {'reactor', 'security', 'lower e', 'medbay', 'cafeteria'},
			'security': {'reactor', 'upper e', 'lower e'},
			'medbay' : {'cafeteria', 'upper e'},
			'admin': {'cafeteria', 'storage'}}

		self.map_crewmate = {
			'cafeteria': {'weapons': 1, 'upper e': 7, 'medbay': 2, 'admin': 2, 'storage': 2},
			'weapons': {'cafeteria': 1, 'o2': 2, 'navigations': 5, 'shield': 7},
			'navigations': {'o2': 3, 'weapons': 5, 'shield': 6},
			'o2': {'weapons': 2, 'navigations': 3, 'shield': 7},
			'shield': {'weapons': 7, 'o2': 7, 'navigations': 6, 'communication': 1, 'storage': 3},
			'communication': {'shield': 1, 'storage': 2},
			'storage': {'communication': 2, 'shield': 3, 'admin': 1, 'cafeteria': 2, 'electrical': 4, 'lower e': 8},
			'electrical': {'storage': 4, 'lower e': 5},
			'lower e': {'storage': 8, 'electrical': 5, 'security': 4, 'reactor': 3, 'upper e': 6},
			'reactor': {'security': 3, 'upper e': 3, 'lower e': 3},
			'upper e': {'reactor': 3, 'security': 3, 'lower e': 6, 'medbay': 5, 'cafeteria': 7},
			'security': {'reactor': 3, 'upper e': 3, 'lower e': 4},
			'medbay' : {'cafeteria': 2, 'upper e': 5},
			'admin': {'cafeteria': 2, 'storage': 1}}
        	
		self.map_impostor = {
			'cafeteria': {'weapons': 1, 'upper e': 7, 'medbay': 2, 'admin': 0, 'storage': 2, 'o2': 3, 'navigations': 3, 'shield': 3},
			'weapons': {'cafeteria': 1, 'o2': 2, 'navigations': 0, 'shield': 7},
			'navigations': {'o2': 3, 'weapons': 5, 'shield': 0},
			'o2': {'weapons': 2, 'navigations': 3, 'shield': 7},
			'shield': {'weapons': 7, 'o2': 7, 'navigations': 0, 'communication': 1, 'storage': 3},
			'communication': {'shield': 1, 'storage': 2},
			'storage': {'communication': 2, 'shield': 3, 'admin': 1, 'cafeteria': 2, 'electrical': 4, 'lower e': 8},
			'electrical': {'storage': 4, 'lower e': 5, 'medbay': 0, 'security': 0},
			'lower e': {'storage': 8, 'electrical': 5, 'security': 4, 'reactor': 0, 'upper e': 6},
			'reactor': {'security': 3, 'upper e': 0, 'lower e': 0},
			'upper e': {'reactor': 0, 'security': 3, 'lower e': 6, 'medbay': 5, 'cafeteria': 7},
			'security': {'reactor': 3, 'upper e': 3, 'lower e': 4, 'electrical': 0, 'medbay': 0},
			'medbay' : {'cafeteria': 2, 'upper e': 5, 'security': 0, 'electrical': 0},
			'admin': {'cafeteria': 0, 'storage': 1, 'o2': 3, 'navigations': 3, 'shield': 3, 'weapons': 4}}

	def bellman_ford(self, graph, source):
		# Step 1: Prepare the distance and predecessor for each node
		distance, predecessor = dict(), dict()
		for node in graph:
			distance[node], predecessor[node] = float('inf'), None
		distance[source] = 0

		# Step 2: Relax the edges
		for i in range(len(graph) - 1):
			for node in graph:
				for neighbour in graph[node]:
					# If the distance between the node and the neighbour is lower than the current, store it
					if distance[neighbour] > distance[node] + graph[node][neighbour]:
						distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

		# Step 3: Check for negative weight cycles
		for node in graph:
			for neighbour in graph[node]:
				assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."
 
		return distance, predecessor        

	def Floyd_Warshall(self, graph):   
		final = list()
		for current_node in graph:       
			final.append(f"'{current_node}': {self.bellman_ford(graph, current_node)[0]}")
		return final

#m = Map([])
#graph = m.Floyd_Warshall(m.map_crewmate)
#for elt in graph:
#	print(elt)

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""

Class Map

"""

class Map:

	def __init__(self):
		"""
		Initialize the map
		:param self: the map itself
		"""
		
		self.map = [
			('cafeteria', 'weapons'), ('cafeteria', 'upper e'), ('cafeteria', 'medbay'), ('cafeteria', 'admin'),
			('cafeteria', 'storage'), ('weapons', 'cafeteria'), ('weapons', 'o2'), ('weapons', 'navigations'),
			('weapons', 'shield'), ('navigations', 'o2'), ('navigations', 'weapons'), ('navigations', 'shield'),
			('o2', 'weapons'), ('o2', 'navigations'), ('o2', 'shield'), ('shield', 'weapons'), ('shield', 'o2'),
			('shield', 'navigations'), ('shield', 'communication'), ('shield', 'storage'), ('communication', 'shield'),
			('communication', 'storage'), ('storage', 'communication'), ('storage', 'shield'), ('storage', 'admin'),
			('storage', 'cafeteria'), ('storage', 'electrical'), ('storage', 'lower e'), ('electrical', 'storage'),
			('electrical', 'lower e'), ('lower e', 'storage'), ('lower e', 'electrical'), ('lower e', 'security'),
			('lower e', 'reactor'), ('lower e', 'upper e'), ('reactor', 'security'), ('reactor', 'upper e'),
			('reactor', 'lower e'), ('upper e', 'reactor'), ('upper e', 'security'), ('upper e', 'lower e'),
			('upper e', 'medbay'), ('upper e', 'cafeteria'), ('security', 'reactor'), ('security', 'upper e'),
			('security', 'lower e'), ('medbay', 'cafeteria'), ('medbay', 'upper e'), ('admin', 'cafeteria'),
			('admin', 'storage')]

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
		
		self.map_int = { 0: [1,3,2,4,5],1:[0,6,7,8],2:[0,3],3:[13,0,12],4:[5,0],5:[0,9,10,8,11,4],6:[1,7,1,8],7:[6,1,8],8:[7,9,5,1,6],9:[5,8],10:[11,5],11:[13,5,3,10,12],12:[11,13,3],13:[11,12,3]}


	def bellman_ford(self, graph, source):
		"""
		Bellman Ford algorithm
		:param self: the map itself
		:param graph: the graph
		:param source: the node from which we look all path to other nodes
		:return: dictionnary of all node from the source node with the distance from it 
		"""
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
		
		return distance  



	def Floyd_Warshall(self, graph):
		"""
		Floyd Warshall Algorithm
		:param self: the map itself
		:param graph: the graph
		:return: all path with cost for all node
		"""
		final = list()
		#we execute bellman_ford for all nodes.
		for current_node in graph:       
			final.append(f"'{current_node}': {self.bellman_ford(graph, current_node)}")
		return final
	


	def hampath(self, graph, start, bound, path=None):
		"""
		recusive Hamiltonian path function
		:param self: the map itself
		:param graph: the graph
		:param start: the first room
		:param bound: the number of rooms
		:param path: the path from the first room to the last
		:return: int path list 
		"""
		
		if path is None:
			path = []

		# If the path is equal to number of point, we pass throught all point and return the path
		if len(path) == bound:
			return path

		# Add the start
		if not path:
			path = path + [start]
			
		# Check candidate
		for candidate in graph[start]:
			# If the canditate is not already in the path, we call de function with the path + the new candidate
			if candidate not in path:
				new_path = self.hampath(graph, candidate, bound, path + [candidate])
				if new_path:
					return new_path



	def Convert_num_to_string(self, list_):
		"""
		Function to convert all int to string, it's more fancy and understanble
		:param self: the map itself
		:param list_: the int list of the path
		:return: none
		"""

		#for each room, we convert the number corresponding to the dedicated room's name
		for elem in list_:

			#exemple : 0 is the cafeteria
			if(elem == 0):
				list_[list_.index(elem)] = "cafeteria"
			if(elem == 1):
				list_[list_.index(elem)] = "weapon"
			if(elem == 2):
				list_[list_.index(elem)] = "medbay"
			if(elem == 3):
				list_[list_.index(elem)] = "upper e" 
			if(elem == 4):
				list_[list_.index(elem)] = "admin" 
			if(elem == 5):
				list_[list_.index(elem)] = "storage" 
			if(elem == 6):
				list_[list_.index(elem)] = "o2"
			if(elem == 7):
				list_[list_.index(elem)] = "navigation" 
			if(elem == 8):
				list_[list_.index(elem)] = "shield" 
			if(elem == 9):
				list_[list_.index(elem)] = "communication"
			if(elem == 10):
				list_[list_.index(elem)] = "electrical"
			if(elem == 11):
				list_[list_.index(elem)] = "lower e"
			if(elem == 12):
				list_[list_.index(elem)] = "security" 
			if(elem == 13):
				list_[list_.index(elem)] = "reactor"



	def print_hampaths(self):
		"""
		function to test a hamiltonian path for each point in a graph (with a different start)
		:param self: the map itself
		"""
		for start in range(1, 14):
			# We test the hamiltonian path for the point
			hamiltonian = self.hampath(self.map_int, start,14)

			# If the algorithm finds a hamiltonian path
			if hamiltonian:
				# prints the path with string
				self.Convert_num_to_string(hamiltonian)
				print("Path : ")
				print(hamiltonian)
				print('')

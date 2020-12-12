#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

from objects.room import *
from objects.player import *

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
		self.rooms = []
		for path in paths:
			with open(path) as inp:
				name = inp[0]
				connected = inp[1]
				vents = inp[2]
				tasks = inp[3]
				sabotage = inp[4]
				form = []
				for i in range(5, len(inp):
					form.append(i)
				r = Room(name, connected, vents, tasks, sabotage)
				self.rooms.append( 
        	self.map_impostor = {
			'cafeteria' : {'weapons' : 1 , 'upper e' : 7 , 'medbay' : 2 , 'admin' : 2 , 'storage' : 2 , 'admin' : 0 },
                	'weapons' : {'cafeteria' : 1, 'o2' : 2 , 'navigation':5, 'shield' : 7 , 'navigation ' : 0 },
                	'navigation' : {'weapons': 0, 'o2' : 3 , 'weapons':5, 'shield' : 7,'shield':0},
                	'o2' : { 'weapon' : 2, 'navigation' : 3,'shield' : 7},
                	'shield' : {'weapons' : 7, 'o2': 7, 'navigation' : 7, 'navigation' : 0, 'communication' : 1, 'storage' : 3},
                	'communication' : { 'shield' : 1 , 'storage' :2},
                	'storage' : { 'communication' : 2,'shield': 3,'admin':1,'cafeteria':2,'electrical':4,'lower e': 8 },
                	'electrical': {'storage':4,'lower e':5,'security':0,'medbay':0},
                	'lower e':{'storage':8,'electrical' : 5,'security': 4,'reactor':4,'upper e':6,'reactor':0},
                	'reactor':{'security': 2,'upper e':3,'lower e':3,'upper e':0,'lower e':0},
                	'upper e':{'reactor':3,'security':3,'lower e':6,'reactor':0,'medbay':5,'cafeteria':7},
                	'security' : {'reactor':3,'upper e':4,'lower e':4,'medbay':0,'electrical':0},
                	'medbay' : {'security':0,'cafeteria':2,'upper e':5}}
        
        	self.map_crewmate = {
            		'cafeteria' : {'weapons' : 1 , 'upper e' : 7 , 'medbay' : 2 , 'admin' : 2 , 'storage' : 2 },
                	'weapons' : {'cafeteria' : 1, 'o2' : 2 , 'navigation':5, 'shield' : 7},
                	'navigation' : {'o2' : 3 , 'weapons':5, 'shield' : 7},
                	'o2' : { 'weapon' : 2, 'navigation' : 3,'shield' : 7},
                	'shield' : {'weapons' : 7, 'o2': 7, 'navigation' : 7, 'communication' : 1, 'storage' : 3},
                	'communication' : { 'shield' : 1 , 'storage' :2},
                	'storage' : { 'communication' : 2,'shield': 3,'admin':1,'cafeteria':2,'electrical':4,'lower e': 8 },
                	'electrical': {'storage':4,'lower e':5},
                	'lower e':{'storage':8,'electrical' : 5,'security': 4,'reactor':4,'upper e':6},
                	'reactor':{'security': 2,'upper e':3,'lower e':3},
                	'upper e':{'reactor':3,'security':3,'lower e':6,'medbay':5,'cafeteria':7},
                	'security' : {'reactor':3,'upper e':4,'lower e':4},
                	'medbay' : {'cafeteria':2,'upper e':5}}

    def bellman_ford(self, graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
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


############ bellman_ford ###################


def Floyd_Warshall(self, graph):   
    final = list()
    for curent_node in graph:       
        final.append(bellman_ford(graph,curent_node)[0])
    return final

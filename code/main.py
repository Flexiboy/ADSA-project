#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.tournament import *
from objects.map import *

def program(choice):
	"""
	Program choice
	:param choice: the choice of the program
	:return: True if a program is selected, False instead
	"""
	if choice == 1:
		#step 1
		print('\nStep 1')
		step1 = Tournament(100)

	elif choice == 2:
		#step 2
		print('\nStep 2')
		print('\nCouple of probable impostors')
		player_list = []
		for i in range(10):
			new_player = Player(i, f'player{i + 1}')
			player_list.append(new_player)
			del new_player
		step2 = Game(player_list)
		print(step2.Couple_probable_impostors_Bellman())

	elif choice == 3:
		#step 3
		print('\nStep 3')
		step3 = Map()
		graph1 = step3.Floyd_Warshall(step3.map_crewmate)
		print('\nMap Crewmate')
		for elt in graph1:
			print(elt)
		graph2 = step3.Floyd_Warshall(step3.map_impostor)
		print('\n\nMap Impostors')
		for elt in graph2:
			print(elt)
		impostor = Player(1,"the impostor")
		impostor.role = "impostor"
		print('\nTime travel for each pair of rooms')
		step3.time_travel(impostor)

	elif choice == 4:
		#step 4
		print('\nStep 4\n')
		print('\nAll paths passing throught each room')
		step4 = Map()
		step4.print_hampaths()

	else:
		#exit
		print('\nExit')
		return False

	return True



def main():
	"""
	The main
	"""
	ctn = True

	while ctn:
		print('\n----- Program choice -----')
		print('1. Step 1')
		print('2. Step 2')
		print('3. Step 3')
		print('4. Step 4')
		print('5. Exit')
		ctn = program(int(input('> ')))



if __name__ == '__main__':
	main()

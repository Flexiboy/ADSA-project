#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN & Valentin FERNANDES

from objects.tournament import *
#from objects.map import *

def program(choice):
	"""
	Program choice
	:param choice: the choice of the program
	:return: True if a program is selected, False instead
	"""
	if choice == 1:
		#step 1
		step1 = Tournament(100)
	elif choice == 2:
		#step 2
		print('step 2')
	elif choice == 3:
		#step 3
		print('step 3')
	elif choice == 4:
		#step 4
		print('step 4')
	else:
		#exit
		print('exit')
		return False
	return True

def main():
	"""
	The main
	"""
	ctn = True

	while ctn:
		print('----- Program choice -----')
		print('1. Step 1')
		print('2. Step 2')
		print('3. Step 3')
		print('4. Step 4')
		ctn = program(int(input('> ')))

if __name__ == '__main__':
	main()

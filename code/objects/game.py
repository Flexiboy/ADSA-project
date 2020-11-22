#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN
# IOS 2 Promo 2022

"""

Class game

"""

import random
import objects.player

class Game:

    def __init__(self,_id,List_player):
        self._id = _id
        self.List_player_impostor = []
        self.List_player_crewmate = []
        i = 0 
        while(i<10):
            rnd = random.randrange(0,9-i, 1)
            if(List_player[rnd] not in List_player_impostor):
                if(i>1):
                    List_player[rnd].role="crewmate"
                    self.List_player_crewmate.append(List_player[rnd])
                
                List_player[rnd].role="impostor"
                self.List_player_impostor.append(List_player[rnd])          
                i+=1


        

    def __str__(self):
        return ( "The game have :\n 2 impostors : " 
        + str(self.List_player_impostor)
        +"\n"
        +"8 crewmates : "
        +str(self.List_player_crewmate)
        )
    
    #def Start(self):
    #    rnd = random.choice([0,1,2,3,4,5,6,7,8,9])


player1 = Player(0,"jacque")
player2 = Player(1,"luc")
player3 = Player(2,"valentin")
player4 = Player(3,"jean")
player5 = Player(4,"brunelle")
player6 = Player(5,"yves")
player7 = Player(6,"martin")
player8 = Player(7,"theo")
player9 = Player(8,"antoine")
player10 = Player(9,"marc")

list_player = [player1,player2,player3,player4,player5,player6,player7,player8,player9,player10]
game1 = Game(0,list_player)
print(game1)
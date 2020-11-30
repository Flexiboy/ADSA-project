#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN
# IOS 2 Promo 2022

"""

Class game

"""

import random

class Game:

    def __init__(self,_id,List_player):
        self._id = _id
        self.List_player_impostor = []
        self.List_player_crewmate = []
        self.List_player = List_player
        i = 0 
        while(i<10):
            rnd = random.randrange(0,9-i, 1)
            if(self.List_player[rnd] not in self.List_player_impostor):
                if(i>1):
                    self.List_player[rnd].role="crewmate"
                    self.List_player_crewmate.append(self.List_player[rnd])
                
                self.List_player[rnd].role="impostor"
                self.List_player_impostor.append(self.List_player[rnd])          
                i+=1


        

    def __str__(self):
        return ( "The game have :\n 2 impostors : " 
        + str(self.List_player_impostor)
        +"\n"
        +"8 crewmates : "
        +str(self.List_player_crewmate)
        )
    
    def Start(self , alive, Task_done = 0):

        if (len(alive)== 4 and self.List_player_impostor[0] in alive and self.List_player_impostor[1] in alive):
            self.List_player_impostor[0].ScoreAdd("win")
            self.List_player_impostor[1].ScoreAdd("win")
            return "Impostors win !"
        if(len(alive)== 2):
            if(self.List_player_impostor[0] in alive or self.List_player_impostor[1] in alive):
                self.List_player_impostor[0].ScoreAdd("win")
                self.List_player_impostor[1].ScoreAdd("win")
                return
        if(self.List_player_impostor[0] not in alive and self.List_player_impostor[1] not in alive):
            for i in self.List_player_crewmate:
                self.List_player_crewmate[i].ScoreAdd("win")
            return "Crewmates win !"
        
        if(Task_done == 8):
            for i in self.List_player_crewmate:
                self.List_player_crewmate[i].ScoreAdd("task_done")
                self.List_player_crewmate[i].ScoreAdd("win")
            return "Crewmates win !"

        rnd_death = bool(random.getrandbits(1)) 
        if(rnd_death == True):
            while True :
                rnd_crewmate = random.choice(range(0, 7, 1))
                rnd_killer = random.choice(range(0,1,1))
                
                if (self.List_player_crewmate[rnd_crewmate] in alive and self.List_player_impostor[rnd_killer] in alive) :
                    alive.pop(self.List_player_crewmate.index(rnd_crewmate))

                    self.List_player_impostor[rnd_killer].AddScore("kill")
                    break
                else : 
                    rnd_crewmate = random.choice(range(0, 7, 1))
                    rnd_killer = random.choice(range(0,1,1))

            rnd_discover_kill = bool(random.getrandbits(1))
            if rnd_discover_kill == True : 
                print(self.List_player_crewmate[rnd_crewmate].name, " is dead, you must vote :")
                vote = self.Vote(alive)
                if(vote == None):
                    print("No one has been ejected")
                else:
                    player_ejected = self.List_player.index(vote)
                    print("player ",player_ejected, " has been ejected")
                    alive.pop(player_ejected)
                    if( player_ejected.role == "impostor"):
                        print(player_ejected.name, " was a impostor")
                        for crewmate in alive:
                            if(crewmate.role == "crewmate"):
                                crewmate.AddScore("unmask_impostor")
            else : 
                for impostor in alive:
                    if(impostor.role == "impostor"):
                        impostor.AddScore("undiscovered_murder")

        while True:           
            rnd_nbplayer_taskdone = random.choice(range(0, 2, 1))
            counter = 0
            while (counter <= rnd_nbplayer_taskdone):
                rnd_crewmate = random.choice(range(0, 7, 1))
                if (self.List_player_crewmate[rnd_crewmate] in alive):
                    self.List_player_crewmate[rnd_crewmate].AddScore("task_done")
                    counter += 1
                else:
                    rnd_crewmate = random.choice(range(0, 7, 1))
            break

        
        return self.Start(alive, Task_done)

    def Vote(self, alive):
        List_votes = []
        result = None
        print("Players still alive : \n")
        for player in alive : 
            print(player.id, ' ', player.name,' ; ')
        print("vote 10 for skip this vote\n")
        for player in alive : 
            print("Player ", player.id, " " , player.name, "vote for : ")
            List_votes.append(int(input()))
        
        max_vote = max(List_votes, key = List_votes.count)
        List_second_max = [value for value in List_votes if value != max_vote]
        second_max_vote = max(List_second_max, key = List_votes.count)

        if(max_vote > second_max_vote and max_vote != 10):
            result = max_vote
        return result
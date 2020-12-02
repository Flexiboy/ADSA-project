#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN
# IOS 2 Promo 2022

"""

Class game

"""

import random

class Game:
    """
    Game constructor

    """
    def __init__(self,_id,List_player):
        self._id = _id
        self.List_player_impostor = []
        self.List_player_crewmate = []
        self.List_player = List_player
        i = 0 

        #loop what places random player in list of crew or impostor and set their role
        while(i<10):
            #take a ramdon player
            rnd = random.randrange(0,9-i, 1)

            #check if the random player isn't in a list (crewmate or impostor) : no occurence
            if(self.List_player[rnd] not in self.List_player_impostor or self.List_player[rnd] not in self.List_player_crewmate):

                #Add first 2 impostors, then add crewmates 
                if(i>1):
                    self.List_player[rnd].role="crewmate"
                    self.List_player_crewmate.append(self.List_player[rnd])
                else :
                    self.List_player[rnd].role="impostor"
                    self.List_player_impostor.append(self.List_player[rnd]) 
                i+=1 
            #If the player si already in a list, take another random index in the player list to take another random player. 
            else :
                rnd = random.randrange(0,9-i, 1)

            


    """
    str function

    return informations about a game
    """    

    def __str__(self):
        return ( "The game have :\n 2 impostors : " 
        + str(self.List_player_impostor)
        +"\n"
        +"8 crewmates : "
        +str(self.List_player_crewmate)
        )
    

    """
    Function to start a game 

    This will play all the game : eliminations, votes, add score, win and lose

    Recursive function for the complexity. each recursivity is a turn in the game

    Take a list of alive players (list of player for the first lauch) and a number of tasks done
    """
    def Start(self , alive, Task_done = 0):

        """
        winner conditionns and adding score

        """
        # If still only 4 players with 2 impostors amoug them, the game is win by impostors
        if (len(alive)== 4 and self.List_player_impostor[0] in alive and self.List_player_impostor[1] in alive):
            #add score
            self.List_player_impostor[0].ScoreAdd("win")
            self.List_player_impostor[1].ScoreAdd("win")
            return "Impostors win !"

        # If still two players with one impostors among them, the game is win by impostors
        if(len(alive)== 2):
            if(self.List_player_impostor[0] in alive or self.List_player_impostor[1] in alive):
                #add score
                self.List_player_impostor[0].ScoreAdd("win")
                self.List_player_impostor[1].ScoreAdd("win")
                return "Impostors win !"

        # If the two impostors are dead (ejected), crewmates win
        if(self.List_player_impostor[0] not in alive and self.List_player_impostor[1] not in alive):
            #add score for each crewmates
            for i in self.List_player_crewmate:
                self.List_player_crewmate[i].ScoreAdd("win")
            return "Crewmates win !"
        
        #if all crewmates have done all tasks (8 crewmates so 8 tasks_done), crewmates win
        if(Task_done == 8):
            #add score for each crewmates
            for i in self.List_player_crewmate:
                self.List_player_crewmate[i].ScoreAdd("task_done")
                self.List_player_crewmate[i].ScoreAdd("win")
            return "Crewmates win !"

        """

        random death

        """

        #take a random bool : if true, a crewmate is dead
        rnd_death = bool(random.getrandbits(1)) 
        if(rnd_death == True):

            #infinite loop
            while True :
                rnd_crewmate = random.choice(range(0, 7, 1))
                rnd_killer = random.choice(range(0,1,1))
                
                # if the random crewmate and impostor is still alive : 
                # pop the crewmate from the alive list 
                # Add the score for the killer
                # break out of the loop
                if (self.List_player_crewmate[rnd_crewmate] in alive and self.List_player_impostor[rnd_killer] in alive) :
                    alive.pop(self.List_player_crewmate.index(rnd_crewmate))

                    self.List_player_impostor[rnd_killer].AddScore("kill")
                    break

                # pick another random killer and crewmate
                else : 
                    rnd_crewmate = random.choice(range(0, 7, 1))
                    rnd_killer = random.choice(range(0,1,1))

            """
            If a crewmate has been killed :
            """
            #take a random bool : if true, the dead crewmate has been discovered and players must vote
            rnd_discover_kill = bool(random.getrandbits(1))            
            if rnd_discover_kill == True : 

                #call the vote function
                print(self.List_player_crewmate[rnd_crewmate].name, " is dead, you must vote :")
                vote = self.Vote(alive)

                #if None, nothing happen
                if(vote == None):
                    print("No one has been ejected")
                else:
                    player_ejected = alive.index(vote)
                    print("player ",player_ejected, " has been ejected")

                    #pop the ejected player from alive list
                    alive.pop(player_ejected)

                    #if the ejected player was impostor, add score
                    if( player_ejected.role == "impostor"):
                        print(player_ejected.name, " was a impostor")
                        for crewmate in alive:
                            if(crewmate.role == "crewmate"):
                                crewmate.AddScore("unmask_impostor")
            
            #If the muder is undiscovered, add scorre
            else : 
                for impostor in alive:
                    if(impostor.role == "impostor"):
                        impostor.AddScore("undiscovered_murder")

        """
        infinite loop for tasks done
        """
        while True:
            #max number of crewmates who have done all tasks is 2            
            rnd_nbplayer_taskdone = random.choice(range(0, 2, 1))
            counter = 0
            while (counter <= rnd_nbplayer_taskdone):

                #Pick a random crewmate
                rnd_crewmate = random.choice(range(0, 7, 1))

                #if crewmate is still alive
                if (self.List_player_crewmate[rnd_crewmate] in alive):
                    self.List_player_crewmate[rnd_crewmate].AddScore("task_done")
                    counter += 1
                
                #else pick another crewmate
                else:
                    rnd_crewmate = random.choice(range(0, 7, 1))

            #break out infinite loop
            break

        #End of the turn, retry with the players still alive
        return self.Start(alive, Task_done)


    """
    Voting method

    Take a list of alive player in the game

    return a None if equality or skip vote majority
    return the index of the player with the max vote in the alive list

    """
    def Vote(self, alive):
        #Set a list of votes. Set a result on None
        List_votes = []
        result = None

        #Print of player still alive
        print("Players still alive : \n")
        for player in alive : 
            if(player.role == "impostor"):
                print(player.id, ' ', player.name,' impostor ',' ; ')
            print(player.id, ' ', player.name,' ; ')
        print("vote 10 for skip this vote\n")

        #request a vote for each player : the player id or 10 for skip
        for player in alive : 
            print("Player ", player.id, " " , player.name, "vote for : ")
            #add the vote to the list
            List_votes.append(int(input()))
        
        #Max occurence of an id : max vote
        max_vote = max(List_votes, key = List_votes.count)
        #Take the second max vote
        List_second_max = [value for value in List_votes if value != max_vote]
        second_max_vote = max(List_second_max, key = List_votes.count)

        #if the mex vote is higher than the second and isn't a skip vote, return the index
        if(max_vote > second_max_vote and max_vote != 10):
            for player in alive:
                if(player.id == max_vote):
                    result = alive.index(player)
        #else return None
        return result

    def Probable_impostors(self,alive,killer,dead):

        
        """

        A finir

        Dict = { } 
        print("Initial nested dictionary:-") 
        print(Dict) 
        
        Dict['Dict1'] = {} 
        
        # Adding elements one at a time  
        Dict['Dict1']['name'] = 'Bob'
        Dict['Dict1']['age'] = 21
        print("\nAfter adding dictionary Dict1") 
        print(Dict) 
        
        # Adding whole dictionary 
        Dict['Dict2'] = {'name': 'Cara', 'age': 25} 
        print("\nAfter adding dictionary Dict1") 
        print(Dict) 

        graph = {'s': {'1': 3, '2': 4},
            '1': {'5': 2, '2': 1, '4':3},
            '2': {'3': 3, '5': 1},
            '3': {'4': 1},
            '4': {'6': 1},
            '5': {'4': 2, '6': 3},
            '6': {}}

        """
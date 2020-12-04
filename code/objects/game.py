#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""

Class game

"""
import random
from player import *

class Game:

    """
    Game constructor

    """
    def __init__(self, _id, list_player):
        self._id = _id
        self.list_player_impostor = []
        self.list_player_crewmate = []
        self.list_player = list_player
        i = 0 

        #loop what places random player in list of crew or impostor and set their role
        while(i<10):
            #take a ramdon player
            rnd = random.randrange(0, 10, 1)

            #check if the random player isn't in a list (crewmate or impostor) : no occurence
            if(self.list_player[rnd] not in self.list_player_impostor and self.list_player[rnd] not in self.list_player_crewmate):

                #Add first 2 impostors, then add crewmates 
                if(i>1):
                    self.list_player[rnd].role="crewmate"
                    self.list_player_crewmate.append(self.list_player[rnd])
                else :
                    self.list_player[rnd].role="impostor"
                    self.list_player_impostor.append(self.list_player[rnd]) 
                i+=1 

            
    """
    str function

    return informations about a game
    """    

    def __str__(self):
        return ( "The game have :\n 2 impostors : " 
        + str(self.list_player_impostor)
        +"\n"
        +"8 crewmates : "
        +str(self.list_player_crewmate)
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
        #if all crewmates have done all tasks (8 crewmates so 8 tasks_done), crewmates win
        if(Task_done == 8):
            #add score for each crewmates
            for crewmate in self.list_player_crewmate:
                crewmate.ScoreAdd("task_done")
                crewmate.ScoreAdd("win")
            print ("All tasks done !")
            print ("Crewmates win !")
            return 0

        """

        random death

        """
        dead_player= []
        #take a random bool : if true, a crewmate is dead
        rnd_death = bool(random.getrandbits(1)) 
        if(rnd_death == True):

            #infinite loop
            while True :
                rnd_crewmate = random.choice(range(0, 8, 1))
                rnd_killer = random.choice(range(0,2,1))
                
                # if the random crewmate and impostor is still alive : 
                # pop the crewmate from the alive list 
                # Add the score for the killer
                # break out of the loop
                if (self.list_player_crewmate[rnd_crewmate] in alive and self.list_player_impostor[rnd_killer] in alive) :
                    alive.pop(alive.index(self.list_player_crewmate[rnd_crewmate]))
                    dead_player.append(self.list_player_crewmate[rnd_crewmate])

                    self.list_player_impostor[rnd_killer].ScoreAdd("kill")
                    break

                # pick another random killer and crewmate
                else : 
                    rnd_crewmate = random.choice(range(0, 8, 1))
                    rnd_killer = random.choice(range(0,2,1))

            # If still only 4 players with 2 impostors amoug them, the game is win by impostors
            if (len(alive)== 4 and self.list_player_impostor[0] in alive and self.list_player_impostor[1] in alive):
                #add score
                self.list_player_impostor[0].ScoreAdd("win")
                self.list_player_impostor[1].ScoreAdd("win")
                print("Unlike bonnie and clyde, nobody caught the impostors. They killed everyone!")
                print ("Impostors win !")
                return 0

            # If still two players with one impostors among them, the game is win by impostors
            if(len(alive)== 2):
                if(self.list_player_impostor[0] in alive or self.list_player_impostor[1] in alive):
                    #add score
                    self.list_player_impostor[0].ScoreAdd("win")
                    self.list_player_impostor[1].ScoreAdd("win")
                    print("The last impostor killed everyone. Like Christophe Lambert he is the highlander !!! Glory to the one")
                    print ("Impostors win !")
                    return 0

            """
            If a crewmate has been killed :
            
            """
            
            #take a random bool : if true, the dead crewmate has been discovered and players must vote
            rnd_discover_kill = bool(random.getrandbits(1))            
            if rnd_discover_kill == True : 

                #call the vote function
                print(self.list_player_crewmate[rnd_crewmate].name, " is dead, you must vote :")
                list_probable_impostors = self.probable_impostors(alive, dead_player)
                print("This the list of probable impostors : ")
                self.Str_list_name(list_probable_impostors)
                vote = self.Vote(alive)
               
                #if None, nothing happen
                if(vote == None):
                    print("No one has been ejected")
                else:
                    player_ejected = alive[vote]
                    print("player ", player_ejected.name, " has been ejected")

                    #pop the ejected player from alive list
                    alive.pop(vote)

                    #if the ejected player was impostor, add score
                    if( player_ejected.role == "impostor"):
                        print(player_ejected.name, " was a impostor")
                        for crewmate in alive:
                            if(crewmate.role == "crewmate"):
                                crewmate.ScoreAdd("unmask_impostor")
            
            #If the muder is undiscovered, add scorre
            else : 
                for impostor in alive:
                    if(impostor.role == "impostor"):
                        impostor.ScoreAdd("undiscovered_murder")
            
                # If the two impostors are dead (ejected), crewmates win
            if(self.list_player_impostor[0] not in alive and self.list_player_impostor[1] not in alive):
                #add score for each crewmates
                for crewmate in self.list_player_crewmate:
                    crewmate.ScoreAdd("win")
                print("All impostors ejected !")
                print ("Crewmates win !")
                return 0

             # If still only 4 players with 2 impostors amoug them, the game is win by impostors
            if (len(alive)== 4 and self.list_player_impostor[0] in alive and self.list_player_impostor[1] in alive):
                #add score
                self.list_player_impostor[0].ScoreAdd("win")
                self.list_player_impostor[1].ScoreAdd("win")
                print("Unlike bonnie and clyde, nobody caught the impostors. They killed everyone!")
                print ("Impostors win !")
                return 0

            # If still two players with one impostors among them, the game is win by impostors
            if(len(alive)== 2):
                if(self.list_player_impostor[0] in alive or self.list_player_impostor[1] in alive):
                    #add score
                    self.list_player_impostor[0].ScoreAdd("win")
                    self.list_player_impostor[1].ScoreAdd("win")
                    print("The last impostor killed everyone. Like Christophe Lambert he is the highlander !!! Glory to the one")
                    print ("Impostors win !")
                    return 0

        """
        infinite loop for tasks done
        """
        while True:
            #max number of crewmates who have done all tasks is 2            
            rnd_nbplayer_taskdone = random.choice(range(0, 2, 1))
            counter = 0
            while (counter < rnd_nbplayer_taskdone):

                #Pick a random crewmate
                rnd_crewmate = random.choice(range(0, 8, 1))

                #if crewmate is still alive
                if (self.list_player_crewmate[rnd_crewmate] in alive):
                    self.list_player_crewmate[rnd_crewmate].ScoreAdd("task_done")
                    counter += 1
                
                #else pick another crewmate
                else:
                    rnd_crewmate = random.choice(range(0, 7, 1))
                Task_done+=1
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
        list_votes = []
        result = None

        #Print of player still alive
        print("Players still alive : \n")
        for player in alive : 
            if(player.role == "impostor"):
                print(player._id, ' ', player.name,' impostor ')
            else:
                print(player._id, ' ', player.name)
        print("vote 10 for skip this vote\n")

        #request a vote for each player : the player id or 10 for skip
        for player in alive : 
            print("Player ", player._id, " " , player.name, "vote for : ")
            #add the vote to the list
            List_votes.append(int(input()))
        
        #Max occurence of an id : max vote
        max_vote_counter = 0
        second_max_vote_counter = 0

        max_vote = max(list_votes, key = list_votes.count)
        for vote in list_votes:
            if(vote == max_vote):
                max_vote_counter+=1

        #Take the second max vote
        list_second_max = [0]
        for value in List_votes:
            if(value != max_vote):
                list_second_max.append(value)

        second_max_vote = max(list_second_max, key = list_second_max.count)
        for vote in list_second_max:
            if(vote == second_max_vote):
                second_max_vote_counter+=1
        
        #if the mex vote is higher than the second and isn't a skip vote, return the index
        if(max_vote_counter > second_max_vote_counter and max_vote != 10):
            for player in alive:
                if(player._id == max_vote):
                    result = alive.index(player)
        #else return None
        return result

    """
    Method to get a graph with all alive player and see the meeting between them.

    We take two lists, alive and dead players.

    return a list of probable impostor (player who was seen with a dead player.)
    """
    def Probable_impostors(self,alive,deads):
        #set graph and lists
        graph = { } 
        list_Probable_impostors = []
        player_turn = alive + deads

        #for each player alive (player who can talk during the vote)
        for player in alive:

            #Set a random number of player saw.
            rnd_players_seen = random.choice(range(1,3,1))
            #If left only two player, the number can only be 0 or 1
            if(len(alive)== 2 ):
                rnd_players_seen = random.choice(range(1,2,1))

            #To the graph, we add a dictionnary for the player
            player_name = player.name
            graph[player_name] = {}

            #For each player seen
            i = 0
            while(i < rnd_players_seen):

                #Choose a random player in all players of the turn (included dead players)
                rnd_player = random.choice(range(0, len(player_turn), 1))

                #if the random player is different of the player (no occurrence)
                if(player_turn[rnd_player] != player): 
                    #Check if the current player didn't see a dead player, check for all deads
                    for dead in deads :
                        if(dead._id == player_turn[rnd_player]._id):
                            #if yes, add the player to the probable impostors list
                            list_Probable_impostors.append(player) 
                    
                    #add the player saw to the dictionnary
                    graph[player_name][player_turn[rnd_player].name] = player_turn[rnd_player]._id
                    i+=1
                else : 
                    rnd_player = random.choice(range(0,len(alive)-1,1))

        print("who saw who? I can help you sherlock : \n", graph)
        return list_Probable_impostors

    """
    Method to print the content of a player list
    """
    def Str_list_name(self, liste):
        if(liste != None):
             for player in liste:
                 print(player.name," ")

    """
    Method to update the score of each player.

    Each time we add a score, it's stored in a list of score. So score for each turn in a game
    is stored

    At the end of a Game, we call the player function Score_game, to addition all scores in one and 
    add it to the Score List of Games (tournement).
    """
    def Update_score_game(self, liste):
        for player in liste:
            player.Score_game()
  
        
p1 = Player(0,'valentin')
p2 = Player(1,'brunelle')
p3 = Player(2,'marc')
p4 = Player(3,'jean')
p5 = Player(4,'steph')
p6 = Player(5,'marie')
p7 = Player(6,'franck')
p8 = Player(7,'antoine')
p9 = Player(8,'lea')
p10 = Player(9,'paul')

Game_players = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

g = Game(1,Game_players)
g.Start(Game_players)
g.Update_score_game(Game_players)
print("")

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Authors: Julien MARTIN-PRIN and Valentin FERNANDES
# IOS 2 Promo 2022

"""
Class game
"""
import random

class Game:

    def __init__(self, _id, list_player):
        """
        Game init
        :param _id: game id
        :param list_player: player list in the game
        """
        self._id = _id
        self.list_player_impostor = []
        self.list_player_crewmate = []
        self.list_player = list_player
        self.alive = []

        random.shuffle(list_player) # shuffling the list to select randomize impostors

        # Delink alive and list_player
        for player in self.list_player:
                self.alive.append(player)

        impostor_count = 2

        # Loop that places random player in list of crew or impostor and set their role
        for player in self.alive:
            rnd_score = random.choice(range(0,13,1))
            if impostor_count > 0:
                impostor_count -= 1
                player.role = "impostor"
                player.Score_games.append(rnd_score)
                self.list_player_impostor.append(player)
            else:
                player.role = "crewmate"
                player.Score_games.append(rnd_score)
                self.list_player_crewmate.append(player)

    def __str__(self):
        """
        Stringify the game object
        :return: increased verbosity of object game
        """
        string =  ("The game have :\n 2 impostors : " 
                + self.Str_list_name(self.list_player_impostor)
                + "\n8 crewmates : "
                + self.Str_list_name(self.list_player_crewmate))
        return string
    

    #region PLAY THE GAME
    def Start(self, task_done = 0, RndVote = True):
        """
        Starting game function
        :param self: the game itself
        :param task: number of accomplished tasks
        :return:
        """
        
        """
        This will play all the game : eliminations, votes, add score, win and lose
        Recursive function for the complexity. each recursivity is a turn in the game
        Take a list of alive players (list of player for the first lauch) and a number of tasks done
        """

        # winner conditionns and adding score

        # if all crewmates have done all tasks (8 crewmates so 8 tasks_done), crewmates win
        if(task_done == 16):
            #add score for each crewmates
            for crewmate in self.list_player_crewmate:
                crewmate.ScoreAdd("task_done")
                crewmate.ScoreAdd("win")
            print ("All tasks done !")
            print ("Crewmates win !")
            return 0

        # random death

        dead_player= []
        #take a random bool : if true, a crewmate is dead
        rnd_death = bool(random.getrandbits(1)) 
        if(rnd_death == True):

            #infinite loop
            while True:
                rnd_crewmate = random.choice(range(0, len(self.list_player_crewmate)-1, 1))
                rnd_killer = random.choice(range(0,len(self.list_player_impostor)-1,1))
                
                # if the random crewmate and impostor is still alive : 
                # pop the crewmate from the alive list 
                # Add the score for the killer
                # break out of the loop
                if (self.list_player_crewmate[rnd_crewmate] in self.alive and self.list_player_impostor[rnd_killer] in self.alive):
                    self.alive.pop(self.alive.index(self.list_player_crewmate[rnd_crewmate]))
                    dead_player.append(self.list_player_crewmate[rnd_crewmate])
                    self.list_player_impostor[rnd_killer].ScoreAdd("kill")
                    break

            # If still only 4 players with 2 impostors amoug them, the game is win by impostors
            if (len(self.alive)== 4 and self.list_player_impostor[0] in self.alive and self.list_player_impostor[1] in self.alive):
                #add score
                self.list_player_impostor[0].ScoreAdd("win")
                self.list_player_impostor[1].ScoreAdd("win")
                print("Unlike bonnie and clyde, nobody caught the impostors. They killed everyone!")
                print ("Impostors win !")
                return 0

            # If still two players with one impostors among them, the game is win by impostors
            if(len(self.alive)== 2):
                if(self.list_player_impostor[0] in self.alive or self.list_player_impostor[1] in self.alive):
                    #add score
                    self.list_player_impostor[0].ScoreAdd("win")
                    self.list_player_impostor[1].ScoreAdd("win")
                    print("The last impostor killed everyone. Like Christophe Lambert he is the highlander !!! Glory to the one")
                    print ("Impostors win !")
                    return 0

            # If a crewmate has been killed :
            
            # take a random bool: if true, the dead crewmate has been discovered and players must vote
            rnd_discover_kill = bool(random.getrandbits(1))            
            if rnd_discover_kill == True: 

                #call the vote function
                print(self.list_player_crewmate[rnd_crewmate].name, " is dead, you must vote :")
                list_probable_impostors = self.Probable_impostors(self.alive, dead_player)
                print("This the list of probable impostors : ")
                self.Str_list_name(list_probable_impostors)
                vote = self.Vote(self.alive,RndVote)
               
                #if None, nothing happen
                if(vote == None):
                    print("No one has been ejected")
                else:
                    player_ejected = self.alive[vote]
                    print("player ", player_ejected.name, " has been ejected")

                    #pop the ejected player from alive list
                    self.alive.pop(vote)

                    #if the ejected player was impostor, add score
                    if( player_ejected.role == "impostor"):
                        print(player_ejected.name, " was a impostor")
                        for crewmate in self.alive:
                            if(crewmate.role == "crewmate"):
                                crewmate.ScoreAdd("unmask_impostor")
            
            #If the muder is undiscovered, add scorre
            else : 
                for impostor in self.alive:
                    if(impostor.role == "impostor"):
                        impostor.ScoreAdd("undiscovered_murder")
            
                # If the two impostors are dead (ejected), crewmates win
            if(self.list_player_impostor[0] not in self.alive and self.list_player_impostor[1] not in self.alive):
                #add score for each crewmates
                for crewmate in self.list_player_crewmate:
                    crewmate.ScoreAdd("win")
                print("All impostors ejected !")
                print ("Crewmates win !")
                return 0
                

             # If still only 4 players with 2 impostors amoug them, the game is win by impostors
            if (len(self.alive)== 4 and self.list_player_impostor[0] in self.alive and self.list_player_impostor[1] in self.alive):
                #add score
                self.list_player_impostor[0].ScoreAdd("win")
                self.list_player_impostor[1].ScoreAdd("win")
                print("Unlike bonnie and clyde, nobody caught the impostors. They killed everyone!")
                print ("Impostors win !")
                return 0

            # If still two players with one impostors among them, the game is win by impostors
            if(len(self.alive)== 2):
                if(self.list_player_impostor[0] in self.alive or self.list_player_impostor[1] in self.alive):
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
                rnd_crewmate = random.choice(range(0, len(self.list_player_crewmate)-1, 1))

                #if crewmate is still alive
                if (self.list_player_crewmate[rnd_crewmate] in self.alive):
                    self.list_player_crewmate[rnd_crewmate].ScoreAdd("task_done")
                    counter += 1
                
                task_done+=1
            #break out infinite loop
            break

        #End of the turn, retry with the players still alive
        return self.Start(task_done)

    def Vote(self, alive,random_vote):
        """
        Voting method
        Take a list of alive player in the game
        return a None if equality or skip vote majority
        return the index of the player with the max vote in the alive list

        if we want manual vote, set the parameter random to False
        """

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

            rnd_player = random.choice(alive)
            print("Player ", player._id, " " , player.name, "vote for : ")
            
            #if we want random vote
            if(random_vote == True):
                #add the vote to the list 
                print(rnd_player._id)
                list_votes.append(rnd_player._id)
            else:
                list_votes.append(int(input()))
        
        #Max occurence of an id : max vote
        max_vote_counter = 0
        second_max_vote_counter = 0

        max_vote = max(list_votes, key = list_votes.count)
        for vote in list_votes:
            if(vote == max_vote):
                max_vote_counter+=1

        #Take the second max vote
        list_second_max = [0]
        for value in list_votes:
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

    def Probable_impostors(self,alive,deads):
        """
        Method to get a graph with all alive player and see the meeting between them.
        We take two lists, alive and dead players.
        return a list of probable impostor (player who was seen with a dead player.)
        """

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

    #endregion

    def Color_player(self,graph):
        """
        Color a graph of player who have seen each other
        :return:player with is color
        """

        # Order nodes in descending degree
        nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
        color_map = {}

        for node in nodes:
            available_colors = [True] * len(nodes)
            for neighbor in graph[node]:
                if neighbor in color_map:
                    color = color_map[neighbor]
                    available_colors[color] = False
                for color, available in enumerate(available_colors):
                    if available:
                        color_map[node] = color
                        break
        return color_map

    def Str_list_name(self, liste):    
        """
        Method to print the content of a player list
        """

        if(liste != None):
             for player in liste:
                 print(player.name," ")

    def Update_score_game(self, liste):
        """
        Method to update the score of each player.
        Each time we add a score, it's stored in a list of score. So score for each turn in a game
        is stored
        At the end of a Game, we call the player function Score_game, to addition all scores in one and 
        add it to the Score List of Games (tournement).
        """
        for player in liste:
            player.Score_game()        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:11:32 2022

@author: alicecampbell

A new 'share with neighbours' method is added to this agentframework file. 
The agent class has been updated to let individual agents have access to 
one another. 

"""


import random

class Agent:
# Have added agents alongside self and environment, allowing agents access
# to eachother. 
    def __init__(self,i, environment, agents):
# the below code allows us to identify each indvidual agent via a name
        self.i = i
        self.environment = environment
        self.agents = agents 
        self.x= random.randint(0,99)
        self.y=random.randint(0,99)
        self.environment = environment 
        self.store = 0 
        
# the below will detail the store of each agent 
    def __str__(self):
        return "i=" + str(self.i) + ", store" + str(self.store) + \
    ', x=' + str(self.x) + ', y=' + str(self.y)
        

    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100


    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0 
        if self.store >= 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0 
            
# The below is a new method for the Communications practical. Will allow agents
#  to look into their 'neighbourhood' (surrounding environment)
    def share_with_neighbours (self, neighbourhood):
# the following allows agents to loop through each other, calculate the distance
# and see the location of other agents. If location is less than or equal to
# the size of the neighbourhood, each agent's store will average the same as in 
# their neighbourhood (by sharing the environment data)
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:
                ave = (self.store + self.agents[i].store) / 2
                self.store = ave
                self.agents[i].store = ave
# following print was used to test that agents were sharing their stores with
# each other
                # print("sharing " + str(distance) + " " + str(ave))
            
    def distance_between(self, agents_row_b):
        return (((self.x - agents_row_b.x)**2) +((self.y - agents_row_b.y)**2))**0.5
   

    
    
    
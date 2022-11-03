#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a separate file for agents. This file will not be able to reflect the 
# environmet in the model file. 


import random

class Agent:
    # I have added 'environment' next to 'self' below, due to a TypeError message 
    # appearing in the IO model file that said:
    #' __init__() takes 1 positional argument but 2 were given'. 
    def __init__(self, environment):
        self.environment = environment
        self.x= random.randint(0,99)
        self.y=random.randint(0,99)
        self.environment = environment 
        self.store = 0
        
    # the below will detail the store of each agent 
    def __str__(self):
        return "store=" + str(self.store) + ', x=' + str(self.x) \
    + ', y=' + str(self.y)
        
# MAKE A MOVE AGENT WITHIN THIS CLASS 

    def move(self):
# following changes the x coordinates
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
# following changes the y coordinates
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

#  below is a new method so that the agents can eat the environment data. If 
# there is 10 in the environment plot, then the agent can gain 10. 

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
            #  the above makes sure that if agents has 'nibbled' too much data 
            # (over 100), they 'dump' the store back onto the environment; 
             # leaving the agents store as 0. 
                
    
    
    
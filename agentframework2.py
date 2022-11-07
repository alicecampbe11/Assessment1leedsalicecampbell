#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Agent framework file for the I/O practical. 

A new 'eat' method has been added to this file, enabling agents to 'nibble' 
and consume data from the imported environment data. The environment is
changed as a result of this. 

'''

import random

# Agent class now calls upon 'environment', so that agents can access the 
# environment data. 

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.x= random.randint(0,99)
        self.y=random.randint(0,99)
        self.environment = environment 
        self.store = 0
        
# the below shows the 'store' (amount of data within) of each agent in the 
# console.
    def __str__(self):
        return "store=" + str(self.store) + ', x=' + str(self.x) \
    + ', y=' + str(self.y)
        

    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

#  below is a new method so that the agents can eat the environment data. If 
# there are '10' bits of data in the environment plot, then the agent can gain
# 10 in its store.

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
                
    
    
    
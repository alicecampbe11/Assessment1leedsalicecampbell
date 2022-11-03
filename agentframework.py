#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is an agent class in a new file. Contains init function - 
# inside this method have created 2 new labels and assigned them 
# random values (x and y).


import random

class Agent:
    # initialiser/constructor of instances of this agent class:
    def __init__(self):
        self.x= random.randint(0,99)
        self.y=random.randint(0,99)
    
        
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


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:48:55 2022

@author: alicecampbell

Agents practical. In this practical the agents are created in the 
'agentframework' file, which creates the agents characteristics and 
behaviour. 

"""


import random
import operator
import matplotlib.pyplot
import agentframework

#random.seed sets the agents to the same number each time the code is run. 
random.seed(0) 
# Below calls upon the agentframework file.
a = agentframework.Agent()
# Below tests whether the creation of agents and their attributes have worked. 
print(a.y,a.x)
a.move()
print(a.y, a.x) 
# 97 49
# 98 48


# The below code function takes in 2 agents, and shows the distance between
 # them.
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 1
agents = []

# The below code creates the agents and prints them as a test.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())
for i in range(num_of_agents):
    print(agents[i].x, agents[i].y)  

# The below code moves the agents. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

print("after move")

# printing agents again to test the move method and check agents have moved from 
# original positions 
for i in range(num_of_agents):
    print(agents[i].x, agents[i].y)  

# The below code creates the graphic.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

# Calling upon the function created at the top of this file. 
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
# test:
# print(distance)
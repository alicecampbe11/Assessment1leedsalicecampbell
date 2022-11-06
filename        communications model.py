#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:49:36 2022

@author: alicecampbell
"""
'''
Communications practical. In this practical each agent will 'get to know
eachother', i.e. go through the agents list, scan their 'neighbourhoods'
(surrounding environment) and 'talk' to close agents  by sharing each 
resources and altering each others variables. 
 
 '''
 
import random
import matplotlib.pyplot
import agentframework3
import csv

environment = []

# the below creates the environment graphic in spyder, using the data from
# an imported csv file.
with open('in.txt', newline='') as f:
     dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
     for row in dataset:
         rowlist = []
         for value in row:
             # print(value)
             rowlist.append(value)
         environment.append(rowlist)            
             

# #random.seed sets the answers to the same number each time the code is run. 
# random.seed(0) 
#  # Below calls upon the agentframework file.
# a = agentframework.Agent(environment, agents)


def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.x - agents_row_b.x)**2) +
     ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []

# Below I have edited the code that makes the agents to allow each agent access
# to the environment:
for i in range(num_of_agents):
     agents.append(agentframework3.Agent(i, environment, agents))
# test (print the agents)
for i in range(num_of_agents):
# print(agents[i].x, agents[i].y)  
         print(agents[i])

# Below code will try to print out an agent from within another agent (0th 
# agent to the 1sr agent), to test that they have access to one another
print( "test")
print(agents[0].agents[1])

# Calling the share with neighbours function from the agent framework file. 
# Created another loop within the iteration, so thatall  agents have  moved 
# before the first agent in the list eats and shares with neighbourhoors. 
# Random shuffle means agents are pricessed not in order. 
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
         agents[i].move()
for j in range(num_of_iterations):
     for i in range(num_of_agents):
         agents[i].move()
         agents[i].eat()
         agents[i].share_with_neighbours(neighbourhood)

print("after move")
 
# printing agents again to test they have moved from 
# original positions
for i in range(num_of_agents):
     # print(agents[i].x, agents[i].y)  
         print(agents[i])


# the below code will show us the environment data being 'nibbled' by the agents.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
     for agents_row_b in agents:
         distance = distance_between(agents_row_a, agents_row_b)
         
         
# below creates a separate file to write out the environments data after being
# 'nibbled' by the agents. This has been displayed in the attachment
# 'environmentout.csv'
with open('environmentout.csv', 'w', newline='') as f2:  
     writer = csv.writer(f2, delimiter=' ')     
     for row in environment:         
         writer.writerow(row) 
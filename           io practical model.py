

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:48:55 2022

@author: alicecampbell


IO practical. This model creates a copy of the environment and a list of the 
agents. Overall this practical lets agents have access to the environment, 
'nibbling' at the environment data.

"""

import random
import matplotlib.pyplot
import agentframework2
import csv

environment = []

# the below creates the environment graphic in spyder, using the data from
# an imported csv file
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            # print(value)
            rowlist.append(value)
        environment.append(rowlist)            
            
# tested that the environment was loading by:
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()

random.seed(0) 
a = agentframework2.Agent(environment)


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 1
agents = []

# Below I have edited the code that makes the agents to allow each agent access
# to the environment:
for i in range(num_of_agents):
    agents.append(agentframework2.Agent(environment))
    # test: 
    # (print the agents)
for i in range(num_of_agents):
    # print(agents[i].x, agents[i].y)  
        print(agents[i])

# Updated the code below so that the 'eat' method is called alongside the move
# method. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

print("after move")

for i in range(num_of_agents):
    # print(agents[i].x, agents[i].y)  
        print(agents[i])


# the below code will show us the environment data being 'nibbled' by the
# agents.
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
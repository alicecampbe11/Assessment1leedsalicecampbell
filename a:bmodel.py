    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
"""
    Created on Fri Nov  4 18:41:42 2022
    
    @author: alicecampbell
 
  
    Created on Wed Nov  2 15:49:36 2022
    
    @author: alicecampbell
  
    Animation/Behaviour (A:B) practical. This practical edits an imported animated
    model file and refines the previously existing code using it. 
     
"""
     
import random
import matplotlib.pyplot 
import agentframework4
import csv
import matplotlib.colors
import matplotlib.animation 

    
environment = []


with open('in.txt', newline='') as f:
         dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
         for row in dataset:
             rowlist = []
             for value in row:
                 # print(value)
                 rowlist.append(value)
             environment.append(rowlist)            
                 
    
def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a.x - agents_row_b.x)**2) +
         ((agents_row_a.y - agents_row_b.y)**2))**0.5
    
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
    

 # Below code is for animation of graphic - creates the figure, axis, and plot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
    


for i in range(num_of_agents):
         agents.append(agentframework4.Agent(i, environment, agents))
    # test (print the agents)
for i in range(num_of_agents):
    # print(agents[i].x, agents[i].y)  
             print(agents[i])
    

print( "test")
print(agents[0].agents[1])
    
carry_on = True	

    
# I have edited the original loop, as the moving of the agents is how the 
# animation will run. Contains the mat plot so the animation runs. Also 
# contains stopping condition.
def update(frame_number):
    
        fig.clear()   
        global carry_on
        
        for j in range(num_of_iterations):
            # random.shuffle(agents)
            random.shuffle(agents)
        for i in range(num_of_agents):
             agents[i].move()
        for i in range(num_of_agents):
             agents[i].move()
             agents[i].eat()
             agents[i].share_with_neighbours(neighbourhood)
# The below is a random stopping condition.
             # if random.random() < 0.1:
             #     carry_on = False
             #     print("stopping condition")
#         store_check = True
 

        stop = False
        count = 0
# The below is a stopping condition for when all agents store is > 70
        for i in range(num_of_agents):
            if (agents[i].store < 70):
                count = count +1
        if count == len(agents):
            print("stopping condition", frame_number)
        carry_on == False 
                
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(environment)
        for i in range(num_of_agents):
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

            
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        

# The below defines the 'gen_function'
def gen_function(b = [0]):
   a = 0
   global carry_on 
   while (a < 10) & (carry_on) :
        yield a			
        a = a + 1

# The below code assigns variables to the animation. A stopping condition 
# stops the animation running infinitely and limits the number of iterations. 
# animation  = matplotlib.animation.FuncAnimation(fig, update, interval=1, \
# repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, \
frames=gen_function, repeat=False)



 # The below outputs the code and creates the animation
matplotlib.pyplot .show()

def gen_function(b = [0]):
   a = 0
   global carry_on 
   while (a < 10) & (carry_on) :
        yield a			
        a = a + 1

    
for agents_row_a in agents:
         for agents_row_b in agents:
             distance = distance_between(agents_row_a, agents_row_b)
             
             
with open('environmentout.csv', 'w', newline='') as f2:  
         writer = csv.writer(f2, delimiter=' ')     
         for row in environment:         
             writer.writerow(row) 
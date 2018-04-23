
# coding: utf-8

# In[4]:


import copy
import numpy as np
from random import *
from IPython.display import clear_output
import sys

width = 0
height = 0
grid = []
up = np.array([0, -1])
down = np.array([0, 1])
left = np.array([-1, 0])
right = np.array([1, 0])
stay = np.array([0, 0])

def clear():
    for f in range(10):
        clear_output(wait=True)
        print(f)

def createmap():
    width = int(input("How wide?"))
    height = int(input("How high?"))
    row = []
    bak = '.'

    
    grid = [['.'] * (width) for height in range(height)]

    #for i in range(width):
     #   row.append(bak)
    
    #for i in range(height):
     #   row2 = copy.deepcopy(row)
      #  grid.append(row2)
        
    return width, height, grid

def playerstart(width, height):
    x = randint(0, width-1)
    y = randint(0, height-1)
    
    playerposition = np.array([x, y])
    
    grid[y][x] = "P"

    print ("You start at ({0},{1})".format((x),(y)))
    
    return playerposition

def printmap():
    while True:
        for i in range(len(grid)):
            print(*grid[i:i+1])
        else: 
            break
    return

def initialize():
    width, height, grid = createmap()
    playerposition = playerstart(width, height)
    printmap()        

def move(playerposition):

    
    return playerposition

def playloop():                
            if data.lower()=="move":
                while True:
                    createmap()
                    printmap()
                    data = input("Where do you want to go UP, DOWN, LEFT, RIGHT, STAY:")
                    if data.lower() not in ('up', 'down', 'left', 'right', 'stay'):
                        print("Not an appropriate choice.")
                        continue
                    else:
                        break
                    if data.lower()=="up":
                        newposition = playerposition+up
                        if newposition[1] < 0:
                            newposition[1] = newposition[1]+len(grid)
                    elif data.lower()=="down":
                        newposition = playerposition+down
                        if newposition[1] > len(grid)-1:
                            newposition[1] = newposition[1]-len(grid)
                    elif data.lower()=="right":
                        newposition = playerposition+right
                        if newposition[0] > width-1:
                            newposition[0] = newposition[0]-width
                    elif data.lower()=="left":
                        newposition = playerposition+left        
                        if newposition[0] < 0:
                            newposition[0] = newposition[0]+width

                    elif data.lower()=="stay":
                        newposition = playerposition+stay

                    if (np.array_equal(playerposition, newposition)):
                        print ("You didnt move")  

                    else:
                        grid[playerposition[1]][playerposition[0]] = " "
                        playerposition = newposition
                        grid[playerposition[1]][playerposition[0]] = "P"
                        print ("You moved to ({0},{1})".format((playerposition[0]),(playerposition[1])))

                    printmap()
    
playloop()



# In[ ]:


#for i in range(height):
#    x = randint(0, width-1)
#    y = randint(0, height-1)
#
#     grid[x][y] = "A""""


# In[ ]:


printmap(createmap())


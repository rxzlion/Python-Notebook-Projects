
# coding: utf-8

# # Simple Game old solution and future use solution

# ## A stupid way to crate a list within a list 
# 
#     This is way work but it is an pythonic.
#     The deepcopy is for copying the orginle list into a new one due to the fact that if you just append the orginle list you
#     just appand a refrrecnce to the same list and you can see that if you look ate the memoery location for each of them.

# In[ ]:


def createmap():
    width = int(input("How wide?"))
    height = int(input("How high?"))
    row = []
    bak = '.'


    for i in range(width):
        row.append(bak)
    
    for i in range(height):
        row2 = copy.deepcopy(row)
        grid.append(row2)
        
    return width, height, grid


# Insted of using the way listed above I just used list comprhnsion

# In[ ]:


def create_map():
    width = int(input("How wide?"))
    height = int(input("How high?"))
   
    grid = [['.'] * (width) for height in range(height)]
        
    return grid


# ## A way to rendomaly change a value inside a list within a list
#     
#     It works and it's not longer or better the the new way but the in the new way I don't need to pass in  width and height
#     into the fuction.

# In[ ]:


def player_start_point(width, height):
    x = randint(0, width-1)
    y = randint(0, height-1)
    
    playerposition = np.array([x, y])
    
    grid[y][x] = "P"

    print ("You start at ({0},{1})".format((x),(y)))
    
    return playerposition


# The new way

# In[3]:


def player_start_point():
    y = random.randrange(0,len(grid))
    x = random.randrange(0,len(grid[y]))
    
    playerposition = np.array([x, y])
    
    return playerposition


# ## A way to clear the console

# In[4]:


from IPython.display import clear_output

def clear():
    for f in range(10):
        clear_output(wait=True)
        print(f)


# ## Initialize function

# In[5]:


def initialize():
    width, height, grid = createmap()
    playerposition = playerstart(width, height)
    printmap()  


# ## Convrted this functions to Classes

#     Convrted the folowing function into classes.
#     Consolidated create_map() and print_map() into one GameMap Classe.
#     Defunct player_start_point() function created a Player Classe instead with an update update_coordinates function.
#     Instead of the player_start_point() I have created a generate_coordinates method inside of the GameMap Classe.
#     The generate_coordinates method will make it esaier to genarte coordinates for other objects in bthe future and makes it
#     esier to acsess the width and height virable.

# ### Old functions

# In[ ]:


def create_map():
    width = int(input("How wide?"))
    height = int(input("How high?"))
   
    grid = [['.'] * (width) for height in range(height)]
        
    return grid

def player_start_point():
    y = random.randrange(0,len(grid))
    x = random.randrange(0,len(grid[y]))
    
    playerposition = np.array([x, y])
    
    return playerposition

def print_map(grid, playerposition):
    grid[playerposition[1]][playerposition[0]] = "P"
    while True:
        for i in range(len(grid)):
            print(*grid[i:i+1])
        else: 
            break
            
    return


# ### New classes

# In[ ]:


class Player:
    
    def __init__(self, coordinates, symbol="P"):
        self.symbol = symbol
        self.coordinates = coordinates
    
    def update_coordinates(self, coordinates):
         self.coordinates = coordinates
                
class GameMap:

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        
        #This isn't strictly necessary, but it clearly introduces these attributes
        self._game_map = None
                
        self.create_map()
        
    def create_map(self):
        self._game_map = [['.'] * (self.width) for height in range(self.height)]
        
    def generate_coordinates(self):
        x = random.randrange(0,self.width)
        y = random.randrange(0,self.height)
        
        coordinates = np.array([x, y])
    
        return coordinates
                         
    def add_object_to_map(self, coordinates, symbol):
        self._game_map[coordinates[1]][coordinates[0]] = symbol
        
    def print_map(self):
        while True:
            for i in range(len(self._game_map)):
                print(*self._game_map[i:i+1])
            else: 
                break


# ## Made a GameObject class

#     Changed the Player class into a base GameObject class and made Player class inherit from the base class.
#     This will make it esiear to ceate other game objects in the future.

# In[ ]:


class GameObject:
    
    def __init__(self, coordinates, symbol=""):
        self.symbol = symbol
        self.coordinates = coordinates
    
    def update_coordinates(self, coordinates):
         self.coordinates = coordinates
            
class Player(GameObject):
    pass


# In[ ]:


class Move:
    
    def up(self, game_object):        
        game_object.new_coordinates["y"] = game_object.coordinates["y"]-game_object.speed
            
    def down(self, game_object):
        game_object.new_coordinates["y"] = game_object.coordinates["y"]+game_object.speed
        
    def left(self, game_object):       
        game_object.new_coordinates["x"] = game_object.coordinates["x"]-game_object.speed
        
    def right(self, game_object):
        game_object.new_coordinates["x"] = game_object.coordinates["x"]+game_object.speed


# In[ ]:


def moving_loop(game_map, move, player):
    while True:
        data = input("Choose an option Up, Down, Left, Right, Exit:")

        if direction.lower() not in ("up", "down", "left", "right", "exit"):
            print("Not an appropriate choice.")
            continue        
           
        if data.lower()=="up":            
            move.up(player)
        elif data.lower()=="down":
            move.down(player)
        elif data.lower()=="left":
            move.left(player)
        elif data.lower()=="right":
            move.right(player)        
        elif data.lower()=="exit":
            raise KeyboardInterrupt
        
        game_map.move_object_on_map(player)
        print (player.coordinates)
        game_map.print_map()


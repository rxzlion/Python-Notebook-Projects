
# coding: utf-8

# In[6]:


import random as random


class NotYetImplemented(Exception):
    """Exception for things not yet implemented"""
    def __init__(self, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = "Code not yet implemented"
        super().__init__(msg)

        
class GameObject:
   
    def __init__(self, coordinates, symbol=None):
        self.symbol = symbol
        self.coordinates = coordinates
        
    def update_coordinates(self, coordinates):
        self.coordinates = coordinates

        
class Move:
    
    def __init__(self, arguments):
        self.coordinates = arguments.coordinates
        self.speed = arguments.speed
                
    def up(self):       
        self.coordinates["y"] -= self.speed
        
    def down(self):
         self.coordinates["y"] += self.speed
        
    def left(self):       
        self.coordinates["x"] -= self.speed
        
    def right(self):
         self.coordinates["x"] += self.speed
        
                 
class Player(GameObject):

    def __init__(self, speed=None, *args, **kwargs):
        self.speed = speed if speed is not None else 1
        super().__init__(*args, **kwargs)
        
        self.move = Move(self)

           
class GameMap:

    def __init__(self, map_size=None):
        self.map_size = map_size
        
        # This isn't strictly necessary, but it clearly introduces these attributes
        self._game_map = None
                
        self.create_map()
        
    def create_map(self):    
        self.map_size = {"width": int(input("How wide?")), "height": int(input("How high?"))}
   
        self._game_map = [['.'] * (self.map_size["width"]) for height in range(self.map_size["height"])]
        
    def generate_coordinates(self):
        x = random.randrange(0,self.map_size["width"])
        y = random.randrange(0,self.map_size["height"])
        
        coordinates = {"x": x, "y": y}
    
        return coordinates
    
    def coordinates_normalization(self, coordinates):
        coordinates = list(coordinates.values())
        map_size = list(self.map_size.values())
        
        for i, (x,y) in enumerate(zip(coordinates, map_size)):
            if x < 0:
                coordinates[i] = y-1
            elif x > y:
                coordinates[i] = 0
            else:
                coordinates[i] = x
                
        coordinates = {"x": coordinates[0], "y": coordinates[1]}
        
        return coordinates    
                             
    def add_object_to_map(self, coordinates, symbol):
        self._game_map[coordinates["y"]][coordinates["x"]] = symbol
        
    def print_map(self):
        while True:
            for i in range(len(self._game_map)):
                print(*self._game_map[i:i+1])
            else: 
                break

def moving_loop(game_map, player):
    while True:
        data = input("Choose an option Up, Down, Left, Right, Exit:")
        
        if data.lower() not in ("up", "down", "left", "right", "exit"):
            print("Not an appropriate choice.")
            continue
        else:
            break
    
    if data.lower()=="up":   
        player.move.up()
        game_map.add_object_to_map(player.coordinates, player.symbol)
        game_map.print_map()
    elif data.lower()=="down":
        player.move.down()
        game_map.add_object_to_map(player.coordinates, player.symbol)
        game_map.print_map()
    elif data.lower()=="left":
        player.move.left()
        game_map.add_object_to_map(player.coordinates, player.symbol)
        game_map.print_map()
    elif data.lower()=="right":
        player.move.right()
        game_map.add_object_to_map(player.coordinates, player.symbol)
        game_map.print_map()
    elif data.lower()=="exit":
        raise KeyboardInterrupt
        
def play_loop():
    while True:
        data = input("Choose an option Start or Exit:")
        
        if data.lower() not in ("start", "exit"):
            print("Not an appropriate choice.")
            continue
        else:
            break
            
    if data.lower()=="start":
        game_map = GameMap()
        player = Player(coordinates=game_map.generate_coordinates(), symbol="P")
        game_map.add_object_to_map(player.coordinates, player.symbol)
        print (player.coordinates)
        game_map.print_map()
        moving_loop(game_map, player)

    elif data.lower()=="exit":
        raise KeyboardInterrupt
    
play_loop()


# # 

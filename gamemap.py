
# coding: utf-8

# In[ ]:


import random as random
import numpy as np


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
            elif x >= y:
                coordinates[i] = 0
            else:
                coordinates[i] = x

        coordinates = {"x": coordinates[0], "y": coordinates[1]}

        return coordinates                
    
    def add_actor_to_map(self, actor):
        self._game_map[actor.coordinates["y"]][actor.coordinates["x"]] = actor.symbol
    
    def move_actor_on_map(self, actor):        
        self.remove_actor_from_map(actor)
        actor.old_coordinates = actor.coordinates
        actor.coordinates = self.coordinates_normalization(actor.new_coordinates)
        self._game_map[actor.coordinates["y"]][actor.coordinates["x"]] = actor.symbol
        
    def remove_actor_from_map(self, actor):
        self._game_map[actor.coordinates["y"]][actor.coordinates["x"]] = '.'
        
    def print_full_map(self):
        while True:
            for i in range(len(self._game_map)):
                print(*self._game_map[i:i+1])
            else: 
                break
        
    def print_small_map(self, actor):
        _game_map = np.asarray(self._game_map)
        _start_y = 0 if actor.coordinates["y"]-5 < 0 else actor.coordinates["y"]-5
        _stop_y = actor.coordinates["y"]+6
        _start_x = 0 if actor.coordinates["x"]-5 < 0 else actor.coordinates["x"]-5
        _stop_x = actor.coordinates["x"]+6
        _small_game_map = _game_map[_start_y:_stop_y,_start_x:_stop_x].tolist()

        while True:
            for i in range(len(_small_game_map)):
                print(*_small_game_map[i:i+1])
            else: 
                break


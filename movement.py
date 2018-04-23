
# coding: utf-8

# In[ ]:


import numpy as np

def walk(actor, vector):
    vectors = {"up": ([0, -1]), "down": ([0, 1]), "left": ([-1, 0]), "right": ([1, 0])}
    coordinates = np.fromiter(actor.coordinates.values(), dtype=int, count=2)
    new_coordinates = coordinates+vectors[vector]*actor.speed
    actor.new_coordinates = {"x": new_coordinates[0], "y": new_coordinates[1]}


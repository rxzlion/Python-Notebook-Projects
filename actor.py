
# coding: utf-8

# In[ ]:


class Actor:
   
    def __init__(self, coordinates, symbol=None):
        self.symbol = symbol
        self.coordinates = coordinates
        self.old_coordinates = {}
        self.new_coordinates = {}


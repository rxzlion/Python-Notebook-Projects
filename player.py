
# coding: utf-8

# In[ ]:


from actor import Actor

class Player(Actor):

    def __init__(self, speed=None, *args, **kwargs):
        self.speed = speed if speed is not None else 1
        super().__init__(*args, **kwargs)
        self.symbol = "P"
        
    def print_stats(self):
        print(self.coordinates)


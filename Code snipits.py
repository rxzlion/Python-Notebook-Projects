
# coding: utf-8

# In[ ]:


#grid with numbring on the side

while True:
    for i in range(len(grid)):
        space = ' '*(len(str(height))-len(str(i+1)))
        if i==0:
            print(*range(1,len(grid)+1))
        print(i+1, space, *grid[i:i+1])
    else:
        break  


# In[ ]:


#No new line in ptrint

print ("hi", end="")
print ("hi")


# In[ ]:


#String formatting

count = 1
conv = count * 2.54
print ('{0} {1}'.format(count, conv))


# In[ ]:


#clone or copy a lis

#You can slice it:

#new_list = old_list[:]
#Alex Martelli's opinion (at least back in 2007) about this is, that it is a weird syntax and it does not make sense to use it ever. ;) (In his opinion, the next one is more readable).

#You can use the built in list() function:

#new_list = list(old_list)

#You can use generic copy.copy():

#import copy
#new_list = copy.copy(old_list)
#This is a little slower than list() because it has to find out the datatype of old_list first.

#If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

#import copy
#new_list = copy.deepcopy(old_list)
#Obviously the slowest and most memory-needing method, but sometimes unavoidable.

#Example:

import copy

class Foo(object):
    def __init__(self, val):
         self.val = val

    def __repr__(self):
        return str(self.val)

foo = Foo(1)

a = ['foo', foo]
b = a[:]
c = list(a)
d = copy.copy(a)
e = copy.deepcopy(a)

# edit orignal list and instance 
a.append('baz')
foo.val = 5

print('original: %r\n slice: %r\n list(): %r\n copy: %r\n deepcopy: %r'
      % (a, b, c, d, e))


# In[ ]:


#Dictionary iterate through values

PIX0 = {"QVGA":"320x240", "VGA":"640x480", "SVGA":"800x600"}
for key in PIX0:
    NUM = input("What is the Resolution of {!r}?".format(key))
    if NUM == PIX0[key]:
        print ("Nice Job!")
        count = count + 1
    else:
        print("I'm sorry but thats wrong. The correct answer was: {!r}.".format(key))

for key, val in PIX0.items():
    NUM = input("Which standard has a resolution of {!r}?".format(val))
    if NUM == key:
        print ("Nice Job!")
        count = count + 1
    else:
        print("I'm sorry but thats wrong. The correct answer was: {!r}.".format(key))


# In[11]:


#install Python Modules

get_ipython().system('python -m pip install matplotlib')


# In[ ]:


kk


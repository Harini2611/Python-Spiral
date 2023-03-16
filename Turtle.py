#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Harini Rajarathinam
#Turtle 


# In[14]:


import turtle

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

turtle.bgcolor('black')
turtle.speed(0)

for i in range(510):
    turtle.pencolor(colors[i % 6])
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(59)
    
turtle.done()


# In[ ]:





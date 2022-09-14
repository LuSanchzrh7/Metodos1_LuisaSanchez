#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


y= lambda x:(np.tan(x))**(1/2)


# In[10]:


x=np.linspace(0.1,1.1,50)


# In[27]:


f=y(x)


# In[28]:


def DerivativeCentral(x,f,h):
    return (-3*f(x)+4*f(x+h)-f(x-2*h))/(2*h)


# In[29]:


def DerivativeP(x,f,h):
    return (-3*f(x)-4*f(x-h)-2*f(x-2*h))/(2*h)


# In[30]:


derC= DerivativeCentral(x,y,0.001)
derP= DerivativeP(x,y,0.001)


# In[31]:


der


# In[33]:


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(2,2,1)
ax.scatter(x,derC)
fig = plt.figure(figsize=(10,10))
ax2 = fig.add_subplot(2,2,1)
ax2.scatter(x,derP)


# In[ ]:





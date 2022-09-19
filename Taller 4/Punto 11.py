#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np



# In[8]:


f= lambda x: np.sqrt(1+np.exp(-x**2))


# In[22]:


def GetSimpson_tres_oct(y, a,b):
    m1= (2*a+b)/3
    m2= (a+2*b)/3
    integral= (b-a)/8*(y(a)+3*y(m1)+3*y(m2)+y(b))
    return integral


# In[23]:


N=100
x= np.linspace(-1,1,N)


# In[27]:


integral=0
for i in range(1,len(x)):
    integral += GetSimpson_tres_oct(f,x[i-1],x[i])
print(integral)






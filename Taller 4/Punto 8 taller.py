#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import sympy as sp


# In[59]:


h= sp.Symbol("h", Real=True)
y_0= sp.Symbol("y_0", Real=True)
y_h= sp.Symbol("y_h", Real=True)
y_2h= sp.Symbol("y_2h", Real=True)
y_3h= sp.Symbol("y_3h", Real=True)


X = np.array([0,h,2*h,3*h])
Y = np.array([y_0,y_h,y_2h,y_3h])


# In[60]:


def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod


# In[61]:


def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum


# In[62]:


x = sp.Symbol('x')
f = Poly(x,X,Y)
f = sp.expand(f)


# In[63]:


f


# In[64]:


a=sp.Symbol("a", Real=True)
b=sp.Symbol("b", Real=True)
int_sp=sp.integrate(f, (x, 0,3*h))


# In[74]:


(sp.simplify(int_sp))
#3/8=0.375


# In[75]:


print("si simpy me dejara sacar el 3/8 y mostrarlo se veria que esta respuesta es satisfactoria, como no se, lo deje asi (pidoperdon)")


# In[ ]:





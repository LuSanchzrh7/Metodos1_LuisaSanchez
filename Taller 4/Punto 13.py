#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import sympy as sym


# In[17]:


def GetLegendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2 - 1)**n
    
    p = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p


# In[45]:


x = sym.Symbol('x',Real=True)
n=2
Legendre=[]
for i in range(n+1):
    
    poly = GetLegendre(i)
    
    Legendre.append(poly)


# In[46]:


Legendre


# In[47]:


a = sym.Symbol('a',Real=True)
b = sym.Symbol('b',Real=True)
c = sym.Symbol('c',Real=True)


# In[54]:


p_0=Legendre[0]*a
p_1=Legendre[1]*b
p_2=Legendre[2]*c


# In[61]:


f_x=5*x


# In[89]:


f_2x=x**2-3


# In[90]:


sym.expand(p_0+p_2)


# In[93]:


res_1=sym.solve([p_1-f_x],[b])


# In[97]:


der_1=sym.diff(p_2+p_0,x)
der_2=sym.diff(f_2x)


# In[99]:


der_1


# In[100]:


res_2=sym.solve([der_1-der_2],[c])


# In[105]:


res_3=sym.solve([p_2+p_0-f_2x,c-res_2[c]],[a,c])

res_3
# In[107]:


res_3


# In[108]:


#entonces
p_0 = sym.Symbol('p_0',Real=True)
p_1 = sym.Symbol('p_1',Real=True)
p_2 = sym.Symbol('p_2',Real=True)
respuesta= res_3[a]*p_0+res_1[b]*p_1+res_2[c]*p_2


# In[110]:


print(respuesta)


# In[ ]:





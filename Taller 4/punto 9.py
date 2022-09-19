#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sympy as sp


# In[13]:


x= sp.Symbol("x",Real=True)
h= sp.Symbol("h",Real=True)
f_d4_xi= sp.Symbol("f^{4}(xi)",Real=True)


# In[14]:


f= (x)*(x-h)*(x-2*h)*(x-3*h)


# In[15]:


int_sp= sp.integrate(f, (x, 0, 3*h))


# In[16]:


int_sp*(f_d4_xi/sp.factorial(4))


# In[ ]:





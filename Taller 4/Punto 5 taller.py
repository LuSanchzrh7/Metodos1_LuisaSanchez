#!/usr/bin/env python
# coding: utf-8

# ## resolver la integral de $\int_0^1 e^{-x^2}$

# In[1]:


# bloque import
import numpy as np


# In[2]:


f=lambda x: np.exp(-x**2)


# In[3]:


class Integrator:
    
    def __init__(self, x,y):
        
        self.x = x
        self.y = y
        self.h = self.x[1] - self.x[0]
        
        self.integral = 0.
    def Trapezoid(self):
        
        self.integral = 0.
        
        self.integral += 0.5*(self.y[0] + self.y[-1])
        
        self.integral += np.sum( self.y[1:-1] )
        
        return self.integral*self.h
    
    def GetTrapezoidError(self,f):
        
        d = (f( self.x + self.h ) - 2*f(self.x) + f( self.x - self.h))/self.h**2 
        
        
        max_ = np.max(np.abs(d))
        
        self.error = (max_* (self.x[-1]-self.x[0])**3 )/(12*(len(self.x)-1)**2)
        
        return self.error


# ### Si se quiere que el error<0.005:

# In[48]:


N = 6
x = np.linspace(0,1,N+1)
y = f(x)


# In[49]:


integral_clase = Integrator(x,y)
#integral_clase.GetTrapezoidError(f)


# In[50]:


valor_int= integral_clase.Trapezoid()


# In[52]:


#valor_int


# In[54]:


print("el valor de la integral es "+str(valor_int)+ "con un error de "+ str(integral_clase.GetTrapezoidError(f)))


# In[ ]:





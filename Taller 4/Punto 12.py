#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import sympy as sym


# In[36]:


def GetNewtonMethod(f,df,xn,itmax = 100000, precision=1e-12):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
        
        except ZeroDivisionError:
            print("zero division")
            
        xn  = xn1
        it += 1
    
    
    if it == itmax:
        return False
    else:
        return xn


# In[37]:


def GetAllRoots(f,df,x, tolerancia=9):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(f,df,i)
          
        if root != False:
            
            croot = np.round( root, tolerancia ) 
            
            if croot not in Roots:
                Roots = np.append( Roots, croot )
                
    Roots.sort()
    
    return Roots


# In[38]:


def GetLegendre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = (x**2 - 1)**n
    
    p = sym.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p


# In[63]:


Legendre = []
DerLegendre = []

x = sym.Symbol('x',Real=True)
n=20

for i in range(n+1):
    
    poly = GetLegendre(i)
    
    Legendre.append(poly)
    DerLegendre.append(sym.diff(poly,x,1))


# In[64]:


def GetRootsPolynomial(n,xi,poly,dpoly):
    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly[n],'numpy')
    dpn = sym.lambdify([x],dpoly[n],'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots


# In[65]:


#para I_2


# In[66]:


xi = np.linspace(-1,1,100)
n = 2
Roots = GetRootsPolynomial(n,xi,Legendre,DerLegendre)


# In[67]:


def GetWeights(Roots,Dpoly):
    
    Weights = []
    x = sym.Symbol('x',Real=True)
    dpn = sym.lambdify([x],Dpoly[n],'numpy')
    
    for r in Roots:
        
        Weights.append( 2/(( 1- r**2 )*dpn(r)**2) )
        
    return Weights


# In[68]:


Weights = GetWeights(Roots,DerLegendre)


# In[69]:


a = 1
b = 2
f = lambda x : 1/(x**2)


# In[70]:


t = 0.5*((b-a)*Roots + a + b)


# In[71]:


Integral = 0.5*(b-a)*np.sum( Weights*f(t) )
Integral


# In[72]:


# para I_3


# In[114]:


n = 3
Roots_t = GetRootsPolynomial(n,xi,Legendre,DerLegendre)
Roots_t=np.append(Roots_t,0)


# In[115]:


Weightst = GetWeights(Roots_t,DerLegendre)
Weightst


# In[116]:


t_t = 0.5*((b-a)*Roots_t + a + b)


# In[117]:


Integral3 = 0.5*(b-a)*np.sum( Weightst*f(t_t) )
Integral3


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





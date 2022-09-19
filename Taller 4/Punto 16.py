#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sym


# In[4]:


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


# In[5]:


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


# In[7]:


def GetLaguerre(n):
    
    x = sym.Symbol('x',Real=True)
    y = sym.Symbol('y',Real=True)
    
    y = sym.exp(-x)*x**n
    
    p = sym.exp(x)*sym.diff(y,x,n)/(np.math.factorial(n))
    
    return p


# In[8]:


Laguerre = []
DerLaguerre = []

x = sym.Symbol('x',Real=True)
n=20

for i in range(n+1):
    
    poly = GetLaguerre(i)
    
    Laguerre.append(poly)
    DerLaguerre.append(sym.diff(poly,x,1))


# In[9]:


def GetRootsPolynomial(n,xi,poly,dpoly):
    
    x = sym.Symbol('x',Real=True)
    
    pn = sym.lambdify([x],poly[n],'numpy')
    dpn = sym.lambdify([x],dpoly[n],'numpy')
    Roots = GetAllRoots(pn,dpn,xi,tolerancia=8)
    
    return Roots


# In[42]:


xi = np.linspace(0,1,100)
n = 3
Roots = GetRootsPolynomial(n,xi,Laguerre,DerLaguerre)


# In[87]:


def GetWeights(Roots,Dpoly):
    
    Weights = []
    x = sym.Symbol('x',Real=True)
    dpn = sym.lambdify([x],Dpoly[n],'numpy')
    
    for r in Roots:
        
        Weights.append( r/(( 1- r**2 )*dpn(r)**2) )
        
    return Weights


# In[186]:


a = 0
b = 72
f = lambda x : (x**3)/(np.exp(x)-1)


# In[187]:


t = 0.5*((b-a)*Roots + a + b)


# In[188]:


Weights = GetWeights(Roots,Laguerre)


# In[189]:


Integral = 0.5*(b-a)*np.sum( Weights*f(t) )


# In[190]:


Integral,(np.pi**4)/15


# In[ ]:





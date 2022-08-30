# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:08:33 2022

@author: issos
"""

#Punto 2 taller derivadas
import numpy as np
import matplotlib.pyplot as plt


#2
N=25
x=np.linspace(-4,4,N)
y=np.linspace(-4,4,N)
h=0.001


    
def derivadax(f,x,y,h): 
    if np.sqrt(y**2+x**2) <= 2:
        return 0
    else:
        return (f(x+h,y)-f(x-h,y))/(2*h)

def derivaday(f,x,y,h):
    if np.sqrt(y**2+x**2) <= 2:
        return 0
    else:
        return (f(x,y+h)-f(x,y-h))/(2*h)

def flujo(x,y):
    return (2*x)-((8*x)/((x**2)+(y**2))) #ecuacion simplificada


#Dibujo Campo V
Vx = np.zeros((N,N))
Vy = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        Vx[i,j] = derivadax(flujo,x[i],y[j],h)
        Vy[i,j] = -(derivaday(flujo,x[i],y[j],h))

Vx = Vx.T
Vy = Vy.T

fig1 = plt.figure(figsize=(8,6))
ax = fig1.add_subplot(1,1,1)

for i in range(1,len(x)):
    for j in range(1,len(y)):
        ax.quiver(x[i],y[j],Vx[i,j],Vy[i,j],color="#0833a2")


#dibujo circulo
punt_circ = 300
R = 2
Orgx = 0
Orgy = 0

theta = np.linspace(0, 2*np.pi, punt_circ+1)
x_circ = R * np.cos(theta) + Orgx
y_circ = R * np.sin(theta) + Orgy
ax.scatter(x_circ,y_circ,color="#f6b44c")
plt.xlabel('x(cm)')
plt.ylabel('y(cm)')

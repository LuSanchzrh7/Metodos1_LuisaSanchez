# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:04:33 2022

@author: issos
"""
#Bloque imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import sympy as sym
from sympy import var, solve
import os.path as path
import wget

#Punto 4
file = 'Parabolico.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file
Data = pd.read_csv(Path_,sep=',')
#print(Data)

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])

def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod

def Poly(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
        
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

#Polinomio que es la trayectoria de la bala (y depende de x)
x_sym = sym.Symbol("x")

y_funcLag = Poly(x_sym,X,Y) #y
dy=sym.diff(y_funcLag, x_sym) #dy/dx
dy2=sym.diff(y_funcLag, x_sym, 2) #dy2/d2x


#hallar valores de primera derivada

dy_numpy=sym.lambdify([x_sym],dy,'numpy')
valor_dy_unopc=dy_numpy(1.4)

#sistema de ecuaciones

theta,vel_cero_cuad=var('x V')

ec_1= sym.tan(theta)+(dy2*1.4)-valor_dy_unopc
respuestatheta= solve([ec_1],[theta])
res_rad=respuestatheta.get(x)
res_grad=res_rad*(180/np.pi)
ec_2= -9.81/((vel_cero_cuad**2)*(sym.cos(res_rad)**2))-dy2
respuestavel= solve([ec_2],[vel_cero_cuad])
V_0=respuestavel[1][0]
Theta_grad=res_grad
print("la velocidad cero(m/s) es:"+str(V_0)+" y el angulo de salida en grados:"+str(Theta_grad))


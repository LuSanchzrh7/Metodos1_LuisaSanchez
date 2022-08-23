# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 08:19:55 2022

@author: issos
"""
import math
import matplotlib.pyplot as plt
import numpy as np

#Punto 5
#1
def fibo_formula(n:int)->int: 
    num=((1+math.sqrt(5))/2)
    ec=(((math.pow(num, n))-(math.pow(1-num,n)))/math.sqrt(5))
    res=round(ec)
    return res
def fibo(n)->int:
    res=n
    if n >= 2:
        res=fibo_formula(n)
    return res

for i in range(0,21):
    print(fibo(i))
#2
x=np.arange(0, 100)
y=[fibo(i) for i in x] 
#print(y)
fig,ax= plt.subplots()
ax.plot(x,y, linewidth=2.0)
"""para grafica logaritmica"""
#plt.yscale("log") 
plt.show()
#3
limite=fibo(1001)
limite_ab=fibo(1000)
res=limite/limite_ab
aureo=res #se aproxima el limite con valores muy altos
print("la respuesta es:"+str(res))
#Punto 5.2
#a
#r=1*theta
dic_polares={}
for i in range(0,360):
    conv=(2*math.pi)/360
    rad= i*(conv)
    dic_polares[rad]=rad
#b
x_carte=[]
y_carte=[]
for i in dic_polares:
    x=(dic_polares.get(i))*math.cos(dic_polares.get(i))
    y=(dic_polares.get(i))*math.sin(dic_polares.get(i))
    x_carte.append(x)
    y_carte.append(y)

plt.scatter(x_carte,y_carte)
plt.show()
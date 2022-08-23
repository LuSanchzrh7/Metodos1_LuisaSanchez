#punto 3.1

def factorial(n:int)->int:
    res=1
    if n != 0:
        for i in range(1,n+1):
            res*=i
    return res
#a
for j in range(0,21):
    ret=factorial(j)
    print(ret)
    
#punto 3.2

def variaciones(n:int,r:int)->int:
    n_fact=factorial(n)
    n_r=n-r
    rest_fact=factorial(n_r)
    res=n_fact/rest_fact
    return res
#a
print(variaciones(6, 3))

#punto 3.3

def combinaciones(n:int,m:int)->int:
    pra_divi=variaciones(n, m)
    segunda_div= 1/(factorial(m))
    res=pra_divi*segunda_div
    return res
#a
print(combinaciones(22, 11))
#b
print(combinaciones(21, 11))
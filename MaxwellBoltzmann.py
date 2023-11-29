import random as r
import math as m
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

vmin=0
vmax=200
pmin=0.0
pmax=1.0
N=100000
T=273.15
M=1*10**(-22)
k=1.38064852*10**(-23)

def func(v):
    a=M/(2*m.pi*k*T)
    b=(-M)*(v**2)/(2*k*T)
    y = 4*m.pi*(v**2)*m.pow(a,1.5)*m.exp(b)
    return y; 

def vfunc(v):
    a=M/(2*m.pi*k*T)
    b=(-M)*(v**2)/(2*k*T)
    y = v*4*m.pi*(v**2)*m.pow(a,1.5)*m.exp(b)
    return y; 

def vvfunc(v):
    a=M/(2*m.pi*k*T)
    b=(-M)*(v**2)/(2*k*T)
    y = v**2*4*m.pi*(v**2)*m.pow(a,1.5)*m.exp(b)
    return y; 

V=[]
FV=[]
P=[]


for i in range(0,N):
    v=r.randrange(vmin,vmax)
    fv=func(v)
    p=r.uniform(pmin,pmax)
    if p<=fv:
        P.append(p)
        V.append(v)
        FV.append(fv)
       
    else:
        continue
        
plt.plot(V,FV,'o', label="Analytical")
weights = np.ones_like(V) / len(V)
plt.hist(V, bins=100, alpha=0.5, label="Random Probability", weights=weights)
plt.xlabel("Velocity", size=14)
plt.ylabel("Count", size=14)
plt.title("Probability vs Boltzmann Maxwell Distribution")
plt.legend(loc='upper right')
plt.show()

x=8*k*T/(M*(m.pi))
y=3*k*T/M


mean_speed=m.pow(x,0.5)
mean_sqspeed=m.pow(y,0.5)


def inte1(v):
    return quad(vfunc, 0, np.inf)

def inte2(v):
    return quad(vvfunc, 0, np.inf)

L1=(inte1(v))
L2=(inte2(v))


print('MEAN SPEED (integral):', L1[0])
print('MEAN SPEED (theoretical):', mean_speed)
print('MEAN SQUARE SPEED (integral):', m.sqrt(L2[0]))
print('MEAN SQUARE SPEED (theoretical):', mean_sqspeed)

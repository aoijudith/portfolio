import random as r
import numpy as np
import pylab
import math as m
import matplotlib as mpl

N=1000

x=np.zeros(N)
y=np.zeros(N)

for i in range(1,N):
    dx=r.randint(-1,1)
    dy=r.randint(-1,1)
    L=m.sqrt(dx**2+dy**2)
    if L>0:
        x[i]=x[i-1]+dx/L
        y[i]=y[i-1]+dy/L
    else:
        continue;


mpl.rcParams['lines.linewidth'] = 0.5
pylab.plot(x, y, markersize=1,marker=".")
pylab.show()

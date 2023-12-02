import random as r
import numpy as np
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt

N=1000

x=np.zeros(N)
y=np.zeros(N)
z=np.zeros(N)

for i in range(1,N):
    dx=r.randint(-1,1)
    dy=r.randint(-1,1)
    dz=r.randint(-1,1)
    L=m.sqrt(dx**2+dy**2+dz**2)
    if L>0:
        x[i]=x[i-1]+dx/L
        y[i]=y[i-1]+dy/L
        z[i]=z[i-1]+dz/L
    else:
        continue


fig = plt.figure()
ax = plt.axes(projection='3d')
mpl.rcParams['lines.linewidth'] = 0.5
ax.plot3D(x, y, z, markersize=1, marker=".")

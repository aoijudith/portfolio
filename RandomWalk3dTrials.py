import random as r
import numpy as np
import math as m


N=1000
Trials=31 #approximate square root of N=1000
R2=[]

for j in range(Trials):
    r.seed(j)
    x=np.zeros(N)
    y=np.zeros(N)
    z=np.zeros(N)
    sum2=np.zeros(N)
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
        sum2=0
        for j in range(N):
            sum2=sum2+(x[i]**2+y[i]**2+z[i]**2)   
        mean2dis=sum2/1000
    R2.append(mean2dis)
    
print(R2)    
mean2disavg=np.sum(R2)/31
print(mean2disavg)

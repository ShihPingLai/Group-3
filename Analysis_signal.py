import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

o = open("in.txt","r")

SigMix=[]

for i in range(1000):
    SigMix.append(float(o.readline()))


t = np.linspace(0, 30, 1000)
"""
plt.plot(t,SigMix)
plt.show()
"""
#Copy the chaos, reproduce signal
#define universal variables
c0 = 15.6
c1 = 1.0
c2 = 28.0
m0 = -1.143
m1 = -0.714

#just a little extra, quite unimportant
def f(x):
    f = m1*x+(m0-m1)/2.0*(abs(x+1.0)-abs(x-1.0))
    return f

#the actual function calculating
def dH_dt(H, t=0):
    return np.array([c0*(H[1]-H[0]-f(H[0])),
                  c1*(H[0]-H[1]+H[2]),
                  -c2*H[1]])

H0 = [0.7, 0.0, 0.0]

H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)


#SigMix-H

out=SigMix-H[:,0]
plt.plot(t,out)
plt.show()


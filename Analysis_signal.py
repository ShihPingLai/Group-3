import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

o1 = open("in1.txt","r")
o2 = open("in2.txt","r")
ot = open("time.txt","r")
SigMix1=[]
SigMix2=[]
t=[]

for i in range(720832):
    SigMix1.append(float(o1.readline()))
    SigMix2.append(float(o2.readline()))
    t.append(float(ot.readline()))



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

out1=SigMix1-H[:,0]*5000
out2=SigMix2-H[:,1]*5000
fig1=plt.figure(1)
plt.plot(t,out1)
plt.show()

fig2=plt.figure(2)
plt.plot(t,out2)
plt.show()


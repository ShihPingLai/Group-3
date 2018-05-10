import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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



#computational time steps
t = np.linspace(0, 30, 1000)
#x, y, and z initial conditions
H0 = [0.7, 0.0, 0.0]

H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)

print(infodict['message'])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:,0], H[:,1], H[:,2])
plt.show()

x = np.sin(t)
plt.plot(t, x)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(H[:,0]+x, H[:,1], H[:,2])
plt.show()

out=H[:,0]+x
#print (out)



f= open("in.txt","w")
for i in range(1000):
    #f.write(str(H[i,0])+" "+str(H[i,1])+" "+str(H[i,2])+" "+"\n")
    #f.write(str(H[i,0]))
    f.write(str(out[i])+"\n")
f.close()


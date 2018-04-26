import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

def fx(c,x,d):
	return c*x+0.5*(d-c)*(abs(x+1)-abs(x-1))

def dx(a,x,y,f,dt):
	return a*(y-x-f)*dt

def dy(x,y,z,dt):
	return (x-y+z)*dt

def dz(B,y,dt):
	return -B*y*dt

#  Set up initial value

c=-0.714
d=-1.143
a=15.6
B=28
x_i=100.0
y_i=100.0
z_i=300.0
dt=0.00001

#  Initialize our result

x=[x_i]
y=[y_i]
z=[z_i]

for j in range(10000000):
	x.append(x[j]+dx(a,x[j],y[j],fx(c,x[j],d),dt))
	y.append(y[j]+dy(x[j],y[j],z[j],dt))
	z.append(z[j]+dz(B,y[j],dt))
"""
print (x)
print (y)
print (z)
"""
#  Plot results

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)
plt.show()




	

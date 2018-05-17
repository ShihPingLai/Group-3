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
#open the data from our sound 
f1= open("sound1.txt","r")
f2= open("sound2.txt","r")
f3= open("time.txt","r")

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
t=[]
sound1=[]
sound2=[]
for i in range (720832):
	t.append(float(f3.readline()))
	sound1.append(float(f1.readline()))
	sound2.append(float(f2.readline()))
#x, y, and z initial conditions
H0 = [0.7, 0.0, 0.0]

H, infodict = integrate.odeint(dH_dt, H0, t, full_output=True)

print(infodict['message'])

#plt.subplot(221)
fig1=plt.figure(1)
ax = fig1.add_subplot(111, projection='3d')
ax.plot(H[:,0]*5000, H[:,1]*5000, H[:,2]*5000)
plt.show()

#plt.subplot(222)
"""
fig2=plt.figure(2)
x = np.sin(t)
plt.plot(t, x)
plt.show()
"""



#plt.subplot(223)
fig3 = plt.figure(3)
ax = fig3.add_subplot(111, projection='3d')
ax.plot(H[:,0]*5000+sound1, H[:,1]*5000+sound2, H[:,2]*5000)
plt.show()

out1=H[:,0]*5000+sound1
out2=H[:,1]*5000+sound2
#print (out)

fig4=plt.figure(4)
plt.plot(t,out1)
plt.show()
fig5=plt.figure(5)
plt.plot(t,sound2)
plt.show()


f4= open("in1.txt","w")
f5= open("in2.txt","w")
for i in range(720832):
    f4.write(str(out1[i])+"\n")
    f5.write(str(out2[i])+"\n")

f4.close()
f5.close()
f1.close()
f2.close()
f3.close()


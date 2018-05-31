#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import wave
import numpy as np
import matplotlib.pyplot as plt


#1 [importing the wav. file, viewing the sound waves and transforming the data into txt. files]
print("Now start reading wave ...")
f1= open("sound1.txt","w")
f2= open("sound2.txt","w")
f3= open("time.txt","w")
def read_wav_data(filename):
    wav = wave.open(filename,"rb") # 打开一个wav格式的声音文件流
    num_frame = wav.getnframes() # 获取帧数
    num_channel=wav.getnchannels() # 获取声道数
    framerate=wav.getframerate() # 获取帧速率
    num_sample_width=wav.getsampwidth() # 获取实例的比特宽度，即每一帧的字节数
    str_data = wav.readframes(num_frame) # 读取全部的帧
    wav.close() # 关闭流
    wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
    wave_data.shape = -1, num_channel # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
    wave_data = wave_data.T # 将矩阵转置
    wave_data = wave_data 
    return wave_data, framerate


def wav_show(wave_data, fs ,title): # 显示出来声音波形
    time = np.arange(0, len(wave_data)) * (1.0/fs)  # 计算声音的播放时间，单位为秒
    # 画声音波形
    plt.plot(time, wave_data)
    plt.title(title)
    plt.show()
print ("Please input the file name of your wav fille 0w0 \n**(No need to type .wav)**")
a = input("File name:")
b = a+".wav"
print ("Saving sound into files ...")  
if(__name__=='__main__'):
	wave_data, fs = read_wav_data(b)  
	wav_show(wave_data[0],fs, 'Channel_1')
	wav_show(wave_data[1],fs, 'Channel_2')  # 如果是双声道则保留这一行，否则删掉这一行
	time = np.arange(0, len(wave_data[0])) * (1.0/fs)
	print("  Writing the sound data into the text files...")
	for i in range(len(wave_data[0])):
		f1.write(str(wave_data[0][i])+"\n")
		f2.write(str(wave_data[1][i])+"\n")	
		f3.write(str(time[i])+"\n")

#print (len(wave_data[0]))

f1.close()
f2.close()
f3.close()

print ("  Done!")

#2 [transforming the text files into list variables]
g1 = open("sound1.txt", "r")
g2 = open("sound2.txt", "r")
g3 = open("time.txt", "r")

sound1 = []
sound2 = []
t = []

print('  Reading the txt. files and creating the list variables...')

for i in range(len(wave_data[0])):
    sound1.append(float(g1.readline()))
    sound2.append(float(g2.readline()))
    t.append(float(g3.readline()))
    
print('  Done!')

g1.close()
g2.close()
g3.close()

#the parameters of generating the chaos
ans = input('Use the default parameters to generate the chaos (y/n)? ')
if ans == 'y':
    c0 = 15.6
    c1 = 1.0
    c2 = 28.0
    m0 = -1.143
    m1 = -0.714
if ans == 'n':
    print('Enter the values of the following parameters: ')
    c0 = float(input('c0 = '))
    c1 = float(input('c1 = '))
    c2 = float(input('c2 = '))
    m0 = float(input('m0 = '))
    m1 = float(input('m1 = '))


#chaos-generating functions calculating
def f(x):
    f = m1*x + (m0-m1)/2.0*(abs(x+1.0)-abs(x-1.0))
    return f

def dH_dt(H, t=0):
    return np.array([c0 * (H[1]-H[0]-f(H[0])),
                  c1 * (H[0]-H[1]+H[2]),
                  -c2 * H[1]])
    

#the initial conditions of x, y, and z
H0 = [0.7, 0.0, 0.0]

H, infodict = integrate.odeint(dH_dt, H0, t, full_output = True)  #這裡的t用到了聲音檔的t

print(infodict['message'])

print ("\n  Signals from the chaos:")

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection = '3d')
ax.plot(H[:,0]*1e05, H[:,1]*1e05, H[:,2]*1e05)
plt.title("Chaos")
plt.show()

plt.plot(t, H[:,0]*1e05)
plt.title("Chaos_x")
plt.show()

plt.plot(t, H[:,1]*1e05)
plt.title("Chaos_y")
plt.show()

#4 [adding sound data to the chaos]

    
out1 = H[:,0]*1e05 + sound1
out2 = H[:,1]*1e05 + sound2
out3 = H[:,2]*1e05

print ("\n  Signals from the mixture:")

fig3 = plt.figure()
ax = fig3.add_subplot(111, projection='3d')
ax.plot(out1, out2, out3)
plt.title("Chaos + Channel_1 + Channel_2")
plt.show()

plt.plot(t, out1)
plt.title("Chaos_x + Channel_1")
plt.show()

plt.plot(t, out2)
plt.title("Chaos_y + Channel_2")
plt.show()

#5 [transforming the result into txt. files]

f4= open("in1.txt", "w")
f5= open("in2.txt", "w")

print("  Writing the data into the text files...")

for i in range(len(wave_data[0])):
    f4.write(str(out1[i]) + "\n")
    f5.write(str(out2[i]) + "\n")
    
print('  Done!')

f4.close()
f5.close()

























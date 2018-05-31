# -*- coding: utf-8 -*-
import wave
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

f1= open("sound1.txt","r")
f2= open("sound2.txt","r")
f3= open("time.txt","r")

framerate = 44100
time = 17

t=[]
sound1=[]
sound2=[]
sound1_np=np.array([0.0]*720832)
sound2_np=np.array([0.0]*720832)

for i in range (720832):
	t.append(float(f3.readline()))
	sound1.append(float(f1.readline()))
	sound2.append(float(f2.readline()))
for k in range(len(sound1)):
	sound1[k]=sound1[k]
	sound2[k]=sound2[k]
for l in range(len(sound1)):
	sound1_np[l]=sound1[l]
	sound2_np[l]=sound2[l]

    
# 产生10秒44.1kHz的100Hz - 1kHz的频率扫描波
#t = np.arange(0, time, 1.0/framerate)
#wave_data = signal.chirp(t, 100, time, 1000, method='linear') * 10000
wave_data1 =sound1_np
wave_data1 = wave_data1.astype(np.short)
# 打开WAV文档
f3 = wave.open(r"sweep1.wav", "wb")

# 配置声道数、量化位数和取样频率
f3.setnchannels(1)
f3.setsampwidth(2)
f3.setframerate(framerate)
# 将wav_data转换为二进制数据写入文件
f3.writeframes(wave_data1.tostring())

wave_data2 =sound2_np
wave_data2 = wave_data2.astype(np.short)
f4 = wave.open(r"sweep2.wav", "wb")
f4.setnchannels(1)
f4.setsampwidth(2)
f4.setframerate(framerate)
f4.writeframes(wave_data2.tostring())



f1.close()
f2.close()
f3.close()
f4.close()


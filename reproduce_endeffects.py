import numpy as np
import librosa
import matplotlib.pyplot as plt
import scipy.signal


sr=16000
##f0=10
##f1=20
f2=5

f3=50

t=np.arange(0,3,1/sr)
#x=-1.2*np.sin(2*np.pi*f0*t)+2*np.cos(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)+10*np.cos(2*np.pi*f3*t)
x=5*np.sin(2*np.pi*f2*t)+np.cos(2*np.pi*f3*t)
plt.subplot(311)
plt.plot(t,x)#,'-.')
#plt.show()


#low pass filter
b,a=scipy.signal.butter(4,Wn=6/(sr/2),btype='lowpass',output='ba')
y=scipy.signal.filtfilt(b,a,x)
plt.subplot(312)
plt.plot(t,y)


#frames' filter
frame_size=win=8000
Y=np.array([])
for i in range(x.shape[0]//win):
    xi=x[i*win:(i+1)*win]
    bi,ai=scipy.signal.butter(4,Wn=6/(sr/2),btype='lowpass',output='ba')
    yi=scipy.signal.filtfilt(bi,ai,xi)
    Y=np.hstack((Y,yi))
time=np.arange(Y.shape[0])/sr
plt.subplot(313)
plt.plot(time,Y,'-.')
plt.show()

"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

####
# Variables & Constants
#===
F1 = 40                 #:Hertz
F2 = 80                 #:Hertz
tInit = 0.0             #:Seconds
tFinal = 0.5            #:Seconds
amp1 = 1
amp2 = 2
numBoxes = 2000
tSpaces = np.linspace(tInit,tFinal,numBoxes)

####
# Initializing Functions
#===
def findOmega(freq):
    omega = 2*np.pi*freq
    return omega

def findFunc(omega1,omega2,time,a1,a2):
    func = a1*np.sin(omega1*time) + a2*np.sin(omega2*time)

    return

####
# Work
#===
wave = findFunc(findOmega(F1),findOmega(F2),tSpaces,amp1,amp2)

t = np.linspace(0,0.5,numBoxes)
w = amp1*np.sin(2*np.pi*F1*t)+amp2*np.sin(2*np.pi*F2*t)

####
# Output Statements
#===
#plt.plot(t,w)
#plt.show()

# Now onto the FFT
fftOut = fft.rfft(w) 

print(len(fftOut))
T=t[1]-t[0]     # sampling rate we chose
N=t.size        # number of time samples
print(t.size)

#1. First we neeed to calculate the absolute value of fftOut, and divide by the number of samples
absFFT = np.abs(fftOut)/N           # these steps are part of the fft algorithm being used
print(len(absFFT))

#plt.plot(fftOut)
#plt.show()

#2. We need to associate a frequency (f) with the coefficients
# Calculate Delta f; this is the frequency spacing for the absFFT array/list
# Expect to obtain Delta f= 2Hz
for i in range(50):
    print("%d  %.3f and %.3f"%(i,absFFT[i],absFFT[i]))     # num20=0.5 -> 40 Hz, and num40=1 -> 80Hz

# let's make the matching frequency array 

freq = np.arange(0,2002,2)
print(freq)
print('length of freq array',len(freq))
#quit()

plt.plot(freq,absFFT)
plt.xlabel('Frequency')
plt.ylabel('FFT')
plt.xlim(0,100)
plt.show()

# 3. "Filter" the low-frequency component
# Note: filter the FFT itself, not the absolute value

# 4. Feed the filtered FFT to irfft()
# This will look like a SHO at 80 Hz
"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
from numpy import pi,sin,cos
import numpy.fft as fft
import matplotlib.pyplot as plt

####
# Variables & Constants
#===
F1 = 40                 #:Hertz
F2 = 80                 #:Hertz
tInit = 0.0             #:Seconds
tFinal = 0.5            #:Seconds
amp1,amp2 = 1,0.5
numBoxes = 2000
tSpaces = np.linspace(tInit,tFinal,numBoxes)

####
# Initializing Functions
#===
def findOmega(freq):
    omega = 2*pi*freq
    return omega

def findFunc(omega1,omega2,time,a1,a2):
    func = a1*sin(omega1*time) + a2*sin(omega2*time)
    return func

####
# Work
#===
omeg1,omeg2 = findOmega(F1),findOmega(F2)
wave = findFunc(omeg1,omeg2,tSpaces,amp1,amp2)

fftOut = fft.rfft(wave)                 #: Finding the FFT

rtSamples = tSpaces[1]-tSpaces[0]       #: Sampling rate we chose
numTSamples = tSpaces.size              #: Number of time samples

#:Part 1 
absFFT = np.abs(fftOut)/numTSamples     #: Absolute Value of the values in the FFT
freq = np.arange(0,2002,2)              #: The matching frequency array

# 3. "Filter" the low-frequency component
fftOutFiltered = fftOut
for i in range(len(fftOutFiltered)):
    
    if fftOutFiltered[i] > 31.35:
        fftOutFiltered[i] = (fftOutFiltered[i-1] + fftOutFiltered[i+1])/2

# 4. Feed the filtered FFT to irfft()
invFFT = fft.irfft(fftOut)
invFFTFiltered = fft.irfft(fftOutFiltered)


####
# Output Statements
#===

#:Part 1 Outputs and Graphs 
plt.plot(tSpaces,wave)
plt.title('Created Time-Domain Function',fontsize=15)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

#:Part 2 Outputs and Graphs 
print('The length of the frequency array is: ',len(freq))
print('The length of the Time-Domain function is: ',len(wave))
print('The length of the Fast Fourier Transform is: ',len(fftOut))
print('The sampling rate is every %.1f seconds and the frequencies are %d and %d Hertz'%((tFinal-tInit),F1,F2))
print('The lengths of f and abs(f) are: %.4f and %.4f.'%(len(fftOut),len(absFFT)))
print('The values for f(N/2) and abs(fft(N/2)) would be specific values rather than lengths')

plt.plot(fftOut)
plt.title('Base FFT (f:0-100)',fontsize=15)
plt.xlabel('Frequency Range')
plt.ylabel('FFT Amplitudes')
plt.xlim(0,100)
plt.show()

plt.plot(freq,absFFT)
plt.title('Absolute Values of FFT (f:0-100)',fontsize=15)
plt.xlabel('Frequency Range')
plt.ylabel('FFT Amplitudes')
plt.xlim(0,100)
plt.show()


#:Part 3 Outputs and Graphs 
print('For the first 25 values: ')
for i in range(25):
    print("%d %.5f, %.5f, and %.5f"%(i,freq[i],fftOut[i],absFFT[i]))


#:Part 4 Outputs and Graphs 
plt.plot(invFFTFiltered)
plt.title('Filtered FFT (f:0-100)',fontsize=15)
plt.xlabel('Frequency Range')
plt.ylabel('FFT Amplitudes')
plt.show()
"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import matplotlib.pyplot as plt
import math as m

####
# Variables & Constants
#===
"""
PI = Constant for numerical pi
amp = Placeholder variable for user's input, set to 1.0 initially
separation = Placeholder variable for user's input, set to 10.0 initially, in cm
boxL = Placeholder variable for the length of one of the box's sides, set to 100.0 initially, in cm
waveL = Placeholder variable for the wavelength, set to 5.0 initially 
pts = Number of data points inside the square image
wvVector = The value of the wavevector
spacing = Amount of space per point
img = Initially empty array with x=y=pts, containing all float values
fileOut = Output file where the image's intensities are placed as a matrix
"""
PI = np.pi
amp = float(1.0)
separation = float(20.0)
boxL = float(100.0)
waveL = float(5.0)
pts = 500
wvVector = 2*PI/waveL
spacing = boxL/pts
img = np.empty([pts,pts],float)
fileOut = 'C:/Users/antho/OneDrive/Documents/GitHub/Applied-Physics/Module-5/A.Shipp-AppliedPhysics-3.2-img.txt'

####
# Initializing Functions
#===
def findCenter(side,sep,num):
    """
    Calculates the waves' initial positions from the side length, 
     separation amount, and which wave is being checked
    """
    if num == 1:
        x = side/2 + sep/2
        y = side/2
    elif num == 2:
        x = side/2 - sep/2
        y = side/2
    return x,y 

def findDistance(xComp,yComp,val1,val2):
    """
    Finds the distance between the wave's center position and the origin
    """
    out = np.sqrt((xComp-val1)**2 + (yComp-val2)**2)
    return out

def findAmpCurrent(ampOrig,vect,rad1,rad2):
    """
    Finds the combined amplitude at a given position in the image
    """
    out = ampOrig*np.sin(vect*rad1) + ampOrig*np.sin(vect*rad2)
    return out

####
# Inputs
#===
separation = float(input('Please input the separation, in cm, the waves will be apart by: '))
boxL = float(input('Please input the side length, in cm, of the square box: '))
waveL = float(input('Please input the wavelength the waves will be: '))
amp = float(input('Please input the amplitude the waves will have: '))

####
# Work
#===
xVal1, yVal1 = findCenter(boxL,separation,1)    #:Finds the center of wave 1
xVal2, yVal2 = findCenter(boxL,separation,2)    #:Finds the center of wave 2

f = open(fileOut, 'w')
for i in range(pts):
    """
    Parses through each position in the image, finds the distance from each waves'
     center positions, then finds the amplitude at that position using the 
     original amplitude, the calculated wavevector, and the distances
    Also prints the image data to fileOut
    """
    y = spacing*i
    f.write('[')
    for j in range(pts):
        x = spacing*j
        r1 = findDistance(x,y,xVal1,yVal1)
        r2 = findDistance(x,y,xVal2,yVal2)
        img[i,j] = findAmpCurrent(amp,wvVector,r1,r2)
        f.write('%f'%img[i,j])
        f.write(', ')
    f.write(']\n')
f.close()

####
# Output Statements
#===
"""
Plots the image
"""
plt.imshow(img, origin='lower', extent=[0,boxL,0,boxL],cmap='Purples')
plt.show()

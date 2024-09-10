"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import astropy as ast
import astropy.constants as cn

####
# Variables & Constants
#===
constRyd = cn.Ryd               #:Rydberg constant 
lmb = float()                   #:Variable used for the wavelengths
m = int()                       #:Principal quantum number of lower energy level
n = int()                       #:Principal quantum number of upper energy level

####
# Initializing Functions
#===
def findLambda(mInput, nInput):
    lmb = 1/(constRyd*((1/mInput**2)-(1/nInput**2)))        #:Puts m&n numbers into the Rydberg formula, then returns the wavelength
    return lmb

####
# Work
#===
print()     #:Adds newline to separate output from filename
for i in range(1,4):                #:Parses through the first 3 principal quantum numbers of the upper energy level
    for j in range(i+1,i+6):        #:Parses through each corresponding first 5 principal quantum numbers of the lower energy level
        lmb = findLambda(i,j)       #:Calls the findLambda function using the upper/lower energy levels' current values
        print('For m=%i and n=%i, the wavelength is: %s' %(i,j,lmb))    #Outputs the information calculated
        j += 1          #Iterates to the next lower energy level
    print() #:Adds newline to separate output depending on the m-levels
    i += 1              #Iterates to the next upper energy level
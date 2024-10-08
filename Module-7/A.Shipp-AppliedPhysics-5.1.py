"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import scipy as sc
from scipy import integrate

####
# Variables & Constants
#===
limitLower = int(0)             #:Lower limit of the integral
limitUpper = int(2)             #:Upper limit of the integral

####
# Initializing Functions
#===
"""
Given Function:
    F(x) = x^{4} + 2x + 1
"""
def equation(x):
    val = x**4 + 2*x + 1
    return val

"""
Finds the trapezoidal estimate of the integral
"""
def trapEstimate(numInput):
    limLow = limitLower
    limUp = limitUpper
    numDx = numInput
    
    sliceWidth = (limUp - limLow)/numDx
    sum = (equation(limUp) + equation(limLow))/2

    for i in range(1,numDx):
        sum += equation(limLow+i*sliceWidth)

    return sum*sliceWidth

####
# Work
#===
"""
Intakes 3 different integers corresponding to the 3 different numbers of slices that will be tested
"""
in1,in2,in3 = input('Please enter three integers for the number of slices to be checked, with a space in between each: ').split()
in1,in2,in3 = int(in1),int(in2),int(in3)
out1,out2,out3 = trapEstimate(in1),trapEstimate(in2),trapEstimate(in3)


####
# Output Statements
#===
print("For N = %i, the integral is %.4f"%(in1,out1))
print("For N = %i, the integral is %.4f"%(in2,out2))
print("For N = %i, the integral is %.4f"%(in3,out3))
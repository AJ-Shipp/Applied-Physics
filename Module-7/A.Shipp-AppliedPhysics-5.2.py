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
from gaussxw import gaussxwab

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
Uses the Gaussian quadrature to find the integral (Using the gaussxwab function)
"""
def gaussInt(numInput):
    limLow = limitLower
    limUp = limitUpper
    numDx = numInput
    sum = float(0)

    samplePts,weights = gaussxwab(numDx,limLow,limUp)

    for i in range(numDx):
        sum += weights[i]*equation(samplePts[i])

    return sum


####
# Work
#===
"""
Intakes 2 different integers corresponding to the 2 different numbers of slices that will be tested
"""
in1,in2 = input('Please enter two integers for the number of slices to be checked, with a space in between each: ').split()
in1,in2 = int(in1),int(in2)
out1,out2 = gaussInt(in1),gaussInt(in2)


####
# Output Statements
#===
print("For N = %i, the integral is %.4f"%(in1,out1))
print("For N = %i, the integral is %.4f"%(in2,out2))
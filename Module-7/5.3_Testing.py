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
from scipy.integrate import quad
from gaussxw import gaussxwab

####
# Variables & Constants
#===
limitLower = int(0)             #:Lower limit of the integral
slices = int(50)                #:Number of slices for each integral
e = np.e                        #:Euler's number
pi = np.pi                      #:Pi

####
# Initializing Functions
#===
"""
Given Function:
    F(x) = x^{4} + 2x + 1
"""
def equation(x):
    val = e**((-x**2)/(2))

    return val

def equationCOV(x,A):
    """
    Using z = x/sqrt(2), then dx = sqrt(2)dz. 
    So int[0,inf] e^(-(x^2)/2) dx = sqrt(2) int[0,inf] e^(-z^2) dz 

    
    
    If z = x/(x+1), then x = z/(z-1)
    Then dz = 1/(x+1)^2 dx, then dx = (x+1)^2 dz



    So int[0,inf] e^(-(x^2)/2) dx = (x+1)^2 int[0,inf] e^(-z^2) dz 
    
    """
    # z = x/(x+1)
    # val = (x+1)**2 * e**(-(z**2)/(2))
    val = quad()

    return val

"""
Uses the Gaussian quadrature to find the integral (Using the gaussxwab function)
"""
def Integrand(x,A):
    ans = A/(e**((-x**2)/(2)))
    return ans

def GaussInt(numInput):
    limLow = limitLower
    numDx = slices
    sum = float(0)
    
    if type(numInput) == type(int()):
        limUp = numInput
        samplePts,wweights = gaussxwab(numDx,limLow,limUp)
        for i in range(numDx):
            sum += wweights[i]*equation(samplePts[i])
        intVal = sum*(np.sqrt((2)/(pi)))
    elif type(numInput) == type(float()):
        # print('pass')
        # limUp = np.inf/(np.inf + 1)
        # samplePts,wweights = gaussxwab(numDx,limLow,limUp)
        # for i in range(numDx):
        #     sum += wweights[i]*equationCOV(samplePts[i])
        # print(sum)
        limLow = 0
        limUp = np.inf

        intVal = quad(Integrand, limLow, limUp,args=(2))

    return intVal


####
# Work
#===
"""
Intakes 3 different integers and 1 string corresponding to the 4 different upper integration bounds will be tested
"""
in1,in2,in3,in4 = input('Please enter the four upper bounds you wish to check, with a space in between each: ').split()
in1,in2,in3,in4 = int(in1),int(in2),int(in3),float(in4)
print(in4,type(in4),in4/in4)
out1,out2,out3,out4 = GaussInt(in1),GaussInt(in2),GaussInt(in3),GaussInt(in4)


####
# Output Statements
#===
print("For N = %i, the integral is %.5f"%(in1,out1))
print("For N = %i, the integral is %.5f"%(in2,out2))
print("For N = %i, the integral is %.5f"%(in3,out3))
print("For N = %s, the integral is %.5f"%(in4,out4))
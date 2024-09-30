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
inputPass = False

####
# Initializing Functions
#===
def checkInt(input):
    allow = False
    inputTrue = float(input)
    inputForce = float(int(input))
    if inputTrue == inputForce:
        allow = True
    
    return allow

def equation(x, dx):
    result = x**4 + 2*x + 1

    return result

####
# Work
#===
while inputPass == False:
    in1,in2,in3 = input('Please enter three integers for the number of slices to be checked, with a space in between each: ').split()
    inputPass1 = checkInt(in1)
    inputPass2 = checkInt(in2)
    inputPass3 = checkInt(in3)

####
# Output Statements
#===
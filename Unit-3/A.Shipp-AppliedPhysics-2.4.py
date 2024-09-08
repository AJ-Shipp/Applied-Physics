"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np

####
# Variables & Constants
#===
numCurr = int(0)                # Pseudo-iterator variable
numA = int(0)                   # Startup value 1
numB = int(1)                   # Startup value 2


####
# Work
#===
print('\nThe terms in the Fibonacci sequence below 1000 are as follows: ')

while numCurr < 1000:
    print(numCurr)
    numCurr = numA + numB
    numA = numB
    numB = numCurr
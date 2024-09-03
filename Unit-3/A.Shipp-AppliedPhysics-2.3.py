"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import astropy as astro
import astropy.constants as const

####
# Variables & Constants
#===
evenNum = int()
oddNum = int()
passAllow = False

####
# Initializing Functions
#===
def evenCheck(xVal,yVal):
    int(xVal)
    int(yVal)
    if (xVal%2 == 0 or yVal%2 == 0) and (xVal & yVal == False) and (xVal != yVal):
        if type(xVal) != int() or type(yVal) != int: #int() does not work to check against
            print(type(xVal), type(yVal))
            print("These numbers are not integers, please try again.")
            exit()
        elif (xVal%2 == yVal%2):
            print("Only one number can be even, and only one can be odd. Please try again.")
        elif xVal%2 == 0:
            evenNum = xVal
            oddNum = yVal
            passAllow = True
        elif yVal%2 == 0: 
            evenNum = yVal
            oddNum = xVal
            passAllow = True
    return 

def checkInt(xInput,yInput):
    xCheck = np.floor(float(xInput))
    yCheck = np.floor(float(yInput))
    returnVal = bool()
    if (xCheck == float(xInput)) and (yCheck == float(yInput)):
        returnVal = True
    else: 
        returnVal = False
    return returnVal

####
# Work
#===
while passAllow == False:
    x,y = input("Enter two integers separated by a space: ").split()
    if x == y:
            print("Please enter two different numbers")
    elif checkInt(x,y) == True:
        evenCheck(int(x),int(y))
    else:
        print("Please be sure to enter two integers.")

####
# Output Statements
#===
print("Of the numbers you entered, the even is %i and the odd is %i"%(evenNum,oddNum))
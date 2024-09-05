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
    output = []
    if (xVal%2 == 0 or yVal%2 == 0) and (xVal & yVal == False) and (xVal != yVal):
        
        # Checks that both the x and y values are integers
        if type(xVal) != type(int(0)) or type(yVal) != type(int(0)): 
            print(type(xVal), type(yVal))
            print("These numbers are not integers, please try again.")
            exit()

        # Checks that the numbers are not both even or both odd 
        elif (xVal%2 == yVal%2):
            print("Only one number can be even, and only one can be odd. Please try again.")
            exit()
        
        # If x is even, places the numbers in output (even first and then odd)
        elif xVal%2 == 0:
            output = [xVal, yVal]
        
        # If y is even, places the numbers in output (even first and then odd)
        elif yVal%2 == 0: 
            output = [yVal, xVal]
    return output

def checkInt(xInput,yInput):
    xCheck = np.floor(float(xInput))
    yCheck = np.floor(float(yInput))
    returnVal = bool()

    # Checks that for x and y, both of them are equal to their values as a floor-rounded float.
    if (xCheck == float(xInput)) and (yCheck == float(yInput)):
        returnVal = True
    else: 
        returnVal = False
    return returnVal

####
# Work
#===
while passAllow == False:

    # Input statement
    x,y = input("Enter two integers separated by a space: ").split()
    
    # Checking if numbers are the same
    if x == y:
            print("Please enter two different numbers")
    
    # When both numbers are integers, checks which is the even or odd, and then exits the loop
    elif checkInt(x,y) == True:
        evenNum, oddNum = evenCheck(int(x),int(y))
        passAllow = True

    # When there are two different numbers, but they aren't both integers, the loop is re-ran
    else:
        print("Please be sure to enter two integers.")

####
# Output Statements
#===
print("Of the numbers you entered, the even is %i and the odd is %i"%(evenNum,oddNum))
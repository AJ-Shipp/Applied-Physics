"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import matplotlib.pyplot as plt

####
# Variables & Constants
#===
fileIn = 'C:/Users/antho/OneDrive/Documents/GitHub/Applied-Physics/Module-5/stars.txt'
method = 0

####
# Initializing Functions
#===

def checkInputType():
    if method == 0:
        file = np.loadtxt(fileIn, float)    
        x = file[:,0]
        y = file[:,1]
    elif method == 1:
        file = np.genfromtxt(fileIn, float)
        x = file[:,0]
        y = file[:,1]
    
    return x,y

def checkLength(first,second):
    l1 = len(first)
    l2 = len(second)

    if l1 == l2:
        print('The two arrays have the same length of', l1, 'entries.')
    else:
        print('The two arrays do not have the same length.')
    
    return

def findAvg(dataList):
    numEntries = 0
    numSum = float()
    average = float()

    for data in dataList:
        curVal = data
        numSum = numSum + curVal
        numEntries += 1
    
    average = numSum / numEntries

    return average


####
# Work
#===
x,y = checkInputType()
checkLength(x,y)
xAvg = findAvg(x)
yAvg = findAvg(y)

plt.scatter(x,y,marker='.')
plt.xlabel('Temperature [K]')
plt.ylabel('Magnitude [m]')
plt.show()

####
# Output Statements
#===
print('The average value of x is: %.2f and the average value of y is: %.2f'%(xAvg,yAvg))
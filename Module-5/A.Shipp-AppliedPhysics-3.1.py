"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

####
# Variables & Constants
#===
fileIn = 'C:/Users/antho/OneDrive/Documents/GitHub/Applied-Physics/Module-5/stars.txt'
method = 0

####
# Initializing Functions
#===
def checkInputType():                   #:Changes file input based on method choice
    if method == 0:
        file = np.loadtxt(fileIn, float)    
        x = file[:,0]
        y = file[:,1]
    elif method == 1:
        file = np.genfromtxt(fileIn, float)
        x = file[:,0]
        y = file[:,1]
    
    return x,y

def checkLength(first,second):          #:Makes sure two lists are the same length
    l1 = len(first)
    l2 = len(second)

    if l1 == l2:
        print('The two arrays have the same length of', l1, 'entries.\n')
    else:
        print('The two arrays do not have the same length.')
    
    return

def findAvg(dataList):                  #:Finds the average of a list of data
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
"""
Creates lists of x and y values. 
Tests their lengths against one another. 
Then finds the averages.
"""
x,y = checkInputType()          
checkLength(x,y)
xAvg = findAvg(x)
yAvg = findAvg(y)


"""
Plotting
"""
plt.scatter(x,y, s=1)                               
plt.xlim(2000,12000)
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.title('Stellar Magnitudes vs Temperatures')
plt.xlabel('Temperature [K]')
plt.ylabel('Magnitude [m]')
plt.xscale('log')
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 12})
plt.rcParams['axes.linewidth'] = 2.0
plt.show()

####
# Output Statements
#===
print('The average value of x is: %.2f and the average value of y is: %.2f'%(xAvg,yAvg))
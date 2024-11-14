"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import scipy as sci
import scipy.stats as scst
import matplotlib.pyplot as plt
from numpy import quantile as qn
from numpy import where as w


####
# Variables & Constants
#===
mu = 100
sigma = 15
numSamples = 1000

####
# Initializing Functions
#===
def findRVS(average,deviation,numTotal):
    imgPlot = scst.norm.rvs(loc=average, scale=deviation, size=numTotal)
    
    return imgPlot

def findPDF(xVals,average,deviation):
    imgPlot = scst.norm.pdf(xVals, loc=average, scale=deviation)
    
    return imgPlot


####
# Work
#===

dataRVS = findRVS(mu,sigma,numSamples)
dataX = np.linspace(0,200,1000)
dataY = findPDF(dataX,mu,sigma)
dataSortRVS = np.sort(dataRVS)

####
# Output Statements
#===

print(
    "This will be a random Gaussian simulation with: \n"
    "Sample Size = {:n}\n"
    "Average = {:n}\n"
    "Error = {:n}\n"
    "\n"
    "| Length            | =   {:n}   \n"
    "| Lower 5% Position | =   {:n}   \n"
    "| Lower 5% Value    | =   {:.2f} \n"
    "| Upper 5% Position | =   {:n}   \n"
    "| Upper 5% Value    | =   {:.2f} \n"
    "| Median Position   | =   {:n}   \n"
    "| Median Value      | =   {:.2f} \n"
    "| Upper Error       | =   {:.2f} \n"
    "| Lower Error       | =   {:.2f} \n"
    .format(numSamples,sigma,mu,len(dataSortRVS),len(dataSortRVS)*0.05,qn(dataSortRVS,0.05),len(dataSortRVS)*0.95,qn(dataSortRVS,0.95),
            len(dataSortRVS)*0.5,qn(dataSortRVS,0.5),qn(dataSortRVS,0.5)-qn(dataSortRVS,0.05),qn(dataSortRVS,0.95)-qn(dataSortRVS,0.5))
    )

plt.hist(dataRVS,bins=20,density=True)
plt.plot(dataX,dataY)
plt.show()

"""
Needs:

Length of the sorted values of the Gaussian distribution: This should be 1000 (the number of samples).

The lower 5% of the sorted samples: At what position in the array does the 5% occur?

The upper 5% of the sorted samples: At what position in the array does the 95% occur?

The median element of the sorted samples: At what position in the array is the middle element?

The lower 5% is at value: What is the 50th value?

The upper 5% is at value: What is the 950th value?

The median value of sorted: What is the 500th value?
"""
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


####
# Variables & Constants
#===
numSamples = 10000

####
# Initializing Functions
#===
def findSamples(lowLim,uppLim,samps,numRVS):
    imgPlot = np.random.uniform(lowLim,uppLim,(samps,numRVS))

    return imgPlot

def findRVS(average,deviation,numTotal):
    imgPlot = scst.norm.rvs(loc=average, scale=deviation, size=numTotal)
    
    return imgPlot

def findPDF(xVals,average,deviation):
    imgPlot = scst.norm.pdf(xVals, loc=average, scale=deviation)
    
    return imgPlot

####
# Work
#===
samples = findSamples(0,2,10000,10)
sums = np.sum(samples,axis=1)
stdDev = np.std(sums)
median = np.median(sums)
confInt = np.percentile(sums,[15.87,84.13])
meanCLT = 10*1
stdDevCLT = np.sqrt(10*(2**2)/12)

dataRVS = findRVS(median,stdDev,numSamples*10)
dataX = np.linspace(0,20,10000)
dataY = findPDF(dataX,median,stdDev)
dataSortRVS = np.sort(dataRVS)

####
# Output Statements
#===
print(
    "From my Simulation: \n"
    "| Standard Deviation  | =   {:.2f} \n"
    "| Median              | =   {:.2f} \n"
    "| Confidence Interval | =   {:.2f} to {:.2f} \n\n"
    "Now from the Central Limit Theorem: \n"
    "| Mean                | =   {:.2f} \n"
    "| Standard Deviation  | =   {:.2f} \n"
    .format(stdDev,median,confInt[0],confInt[1],meanCLT,stdDevCLT)
    )

plt.hist(dataRVS,bins=200,density=True)
plt.plot(dataX,dataY)
plt.show()
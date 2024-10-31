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
mu = 100
sigma = 15
numSamples = 1000


# A=ss.norm(ous)
####
# Initializing Functions
#===
def findRVS(average,deviation,numTotal):
    imgPlot = scst.norm.rvs(loc=average, scale=deviation, size=numTotal)
    
    return imgPlot

def findPDF(average,deviation):
    imgPlot = scst.norm.pdf(loc=average, scale=deviation)
    
    return imgPlot


####
# Work
#===




"""
"""

####
# In-Class Work
#===

mu = 100
sigma = 15
numSamples = 1000

A = scst.norm.rvs(loc=mu, scale=sigma, size=numSamples)
print(A)

plt.hist(A,bins=20,density=True)

# overplot the expected pdf
# accomplish this with scst.norm.pdf

x=np.linspace(0,200,1000)
y=scst.norm.pdf(x,loc=mu,scale=sigma)
plt.plot(x,y)
plt.show()

# there are two ways to get the 0.05, 0.95, and 0.5 quantiles
# use np.quantile()

# The direct (and harder) way: order the measurements, and leave 0.05% to the left, 50% to the left, 
#   and 95% to the left to find the quantiles 
# 
ASort = np.sort(A)
print(ASort)

"""
"""








####
# Output Statements
#===


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
"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scst
from scipy.stats import chi2 as c2
import scipy.optimize as scop
from scipy.optimize import curve_fit as cf

####
# Variables & Constants
#===
valX = np.array([0,2,3,4,5])
valY = np.array([0,4,11,14,23.5])
errorY = np.array([1,2,1,1.5,2.5])

####
# Initializing Functions
#===
def function(x,a,b):
    out = a+b*x

    return out

####
# Work
#===

#####
# In-Class
#===
params,cov = cf(function,valX,valY,sigma=errorY,p0=[0,0],absolute_sigma=True)

print("Params",params)
print("Cov",cov)

for i in range(2):
    print('%3.3f +- %3.3f'%(params[i],cov[i,i]**0.5))

plt.plot(valX,valY,'b-',label='data')
plt.errorbar(valX,valY,fmt='o',yerr=[errorY,errorY],capsize=2)
plt.xlabel('x')
plt.ylabel('y')
yplot=np.zeros(5)
for i in range(5):
    yplot[i] = function(valX[i],params[0],params[1])
plt.plot(valX,yplot,'r-',label='best-fit linear model')
plt.legend()
plt.show()


#Add chhi^2 statistic and determine if it is a good fit 
chi = ((valY-yplot)/errorY)**2
chiMin=sum(chi)
print('Chi2: ',chiMin)
f=3

#Percentile function, inverse of CDF
chiCrit = c2.ppf(0.9,3)
print('Critical Value: ',chiCrit)
if (chiMin > chiCrit):
    print('==> Hypothesis rejected')
else: 
    print('==> Hypothesis acceptable')

####


####
# Output Statements
#===
# plt.plot(valX,valY)
# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# plt.errorbar(valX,valY,yerr=errorY,capsize=5)
# plt.show()

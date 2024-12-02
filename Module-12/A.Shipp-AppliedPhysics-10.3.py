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
valX = np.array([0,2,3,4,5])                #:Chart's X Values
valY = np.array([0,4,11,14,23.5])           #:Chart's Y Values
errorY = np.array([1,2,1,1.5,2.5])          #:Chart's Error Values
yplot=np.zeros(5) 


####
# Initializing Functions
#===
def function(x,a,b):
    out = a+b*x

    return out

def hypCheck(chMin, chCrit):
    if (chMin > chCrit):
        hypResults = '==> Rejected'
    else: 
        hypResults = '==> Acceptable'
    
    return hypResults


####
# Work
#===
params,cov = cf(function,valX,valY,sigma=errorY,p0=[0,0],absolute_sigma=True) 
chi = ((valY-yplot)/errorY)**2 
chiMin=sum(chi) 
chiCrit = c2.ppf(0.9,3) 
for j in range(5): 
    yplot[j] = function(valX[j],params[0],params[1]) 
results = hypCheck(chiMin,chiCrit) 


####
# Output Statements
#===
print(
    "\nThe Best-Fit Parameters are: \n"
    "{:.6f} and {:.6f} \n\n"
    "The Covariance Matrix is: \n"
    "{} \n\n"
    "The (Chi)^2 Critical Values are: \n"
    "{:3.3f} +/- {:3.3f} \n"
    "       and          \n"
    " {:3.3f} +/- {:3.3f} \n\n"
    "The (Chi)^2 Value itself is: \n"
    "{:3.3f} \n\n"
    "The Critical Value is: \n"
    "{:3.3f} \n\n"
    "Ultimately, the fit was: \n"
    "{} \n"
    .format(params[0],params[1],cov,params[0],cov[0,0]**(0.5),params[1],cov[1,1]**(0.5),chiMin,chiCrit,results)
    )


#####
# In-Class
#===
plt.plot(valX,valY,'b-',label='Datapoints')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.errorbar(valX,valY,fmt='o',yerr=[errorY,errorY],capsize=5)
plt.plot(valX,yplot,'r-',label='Best-Fit Model (Linear)')
plt.legend()
plt.show()


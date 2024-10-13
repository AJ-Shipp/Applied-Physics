"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np 
from numpy import linalg as lna

####
# Variables & Constants
#===
mtrx = np.array([])
mtrxA = np.array([[-1.,2.,1.],[2.,3.,0.],[1.,0.,3.]])
mtrxB = np.array([[-1.,1.,3.],[1.,2.,0.],[3.,0.,2.]])
mtrxC = np.array([[-3.,2.,2.],[2.,1.,3.],[2.,3.,1.]])
validIn = False

####
# Initializing Functions
#===
def checkInput(inp):
    out = False
    mtrx = np.array([])
    if inp == 'a' or 'b' or 'c':
        out = True
        if inp == 'a':
            mtrx = mtrxA
        elif inp == 'b':
            mtrx = mtrxB
        elif inp == 'c':
            mtrx = mtrxC
    return out, mtrx

####
# Work
#===
while validIn == False:
    select = input("Would you like to view the data for Matrix A, B, or C? (Please enter a single letter a/b/c): ")
    validIn,mtrx = checkInput(select)

inv = lna.inv(mtrx)
eigVal,eigVec = lna.eig(mtrx)
invEigVec = lna.inv(eigVec)
diag = lna.matmul(lna.matmul(invEigVec,mtrx),eigVec)

####
# Output Statements
#===
print("1",mtrx)
print("2",inv)
print("3",eigVal)
print("4",eigVec)
print("5",invEigVec)
print("6",np.round(diag))
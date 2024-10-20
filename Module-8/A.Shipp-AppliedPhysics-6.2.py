"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
from numpy import linalg as lna
import cmath as cm
np.set_printoptions(suppress=True)

####
# Variables & Constants
#===
PI = np.pi
RES1 = RES2 = 1000      #:Ohms
OMEGA = 1000            #:Hz
CAP = 1e-6              #:Micro-Farads
VLT1 = 100              #:Volts
INDCT = 1               #:Henrys
CRRNT1,CRRNT2,CRRNT3 = 1,1,1    #:Amps

circuitCAP = np.array([[CRRNT1,-CRRNT2,-CRRNT3],[RES1,RES2,0],[0,RES2,-1j/(OMEGA*CAP)]],dtype=complex)
circuitINDCT = np.array([[CRRNT1,-CRRNT2,-CRRNT3],[RES1,RES2,0],[0,RES2,1j*OMEGA*INDCT]],dtype=complex)
equivARRAY = np.array([[0],[VLT1],[0]],dtype=complex)
currARRAY = np.array([["I1"],["I2"],["I3"]])
validIn = False
prntEq = int()
"""
Capacitor:
1. I1 = I2 + I3 --> I1 - I2 - I3 = 0
2. V1 - I1R1 - I2R2 = 0
3. (I2R2) - (i/wC)*I3 = 0 --> V1 - I1R1 - (i/wC)*R3 = 0

Inductor:
1. I1 = I2 + I3 --> I1 - I2 - I3 = 0
2. V1 - I1R1 - I2R2 = 0
3. (I2R2) - iwL*I3 = 0 --> V1 - I1R1 - iwL*R3 = 0
"""

####
# Initializing Functions
#===
def checkInput(inp=str()):
    out = False
    mtrx = np.array([])
    input = inp.lower()
    pEq = 3

    if input == 'c' or input == 'l':
        out = True
        if input == 'c':
            mtrx = circuitCAP
            pEq = 0
        elif input == 'l':
            mtrx = circuitINDCT
            pEq = 1
    else:
        print("Please Try Again.")
    
    return out,mtrx,pEq

def findMag(x,y):
    mag = np.sqrt((x)**2 + (y)**2)
    mag = np.round(mag,decimals=3)
    return mag

####
# Work
#===
while validIn == False:
    select = input("\nWould you like to solve the circuit with the capacitor or inductor? (Please enter a single letter C/L): \n")
    validIn,mtrx,prntEq = checkInput(select)

X=lna.solve(mtrx,equivARRAY)

####
# Output Statements
#===
print(
    "\nYou wish to solve the linear equation Ax=B with, \n"
    "A)\n{}\n"
    "x)\n{}\n"
    "B)\n{}\n".format(mtrx,currARRAY,equivARRAY)
    )

if prntEq == 0:
    print(
        "This gives us:\n"
        "[  (1+0j)*I1   +  (-1+0j)*I2  +   (-1+0j)*I3  ] =     0j    \n"
        "[ (1000+0j)*I1 + (1000+0j)*I2 +    (0j)*I3    ] =  (100+0j) \n"
        "[ (1000+0j)*I1 +    (0j)*I2   + (-1000+0j)*I3 ] =  (100+0j) \n\n"
        )
elif prntEq == 1:
    print(
        "This gives us:\n"
        "[  (1+0j)*I1   +  (-1+0j)*I2  +   (-1+0j)*I3  ] =     0j    \n"
        "[ (1000+0j)*I1 + (1000+0j)*I2 +    (0j)*I3    ] =  (100+0j) \n"
        "[ (1000+0j)*I1 +    (0j)*I2   +  (0+1000j)*I3 ] =  (100+0j) \n\n"
        )

print(
    "The solution is: "
    "\n I1 = {} \n    or {} A with phase =  {} degrees"
    "\n I2 = {} \n    or {} A with phase = {} degrees"
    "\n I3 = {} \n    or {} A with phase =  {} degrees\n"
    .format(
    X[0],findMag(X[0][0].real,X[0][0].imag),np.round(-cm.phase(X[0][0])*(360/(2*PI)),decimals=3),
    X[1],findMag(X[1][0].real,X[1][0].imag),np.round(-cm.phase(X[1][0])*(360/(2*PI)),decimals=3),
    X[2],findMag(X[2][0].real,X[2][0].imag),np.round(-cm.phase(X[2][0])*(360/(2*PI)),decimals=3))
    )
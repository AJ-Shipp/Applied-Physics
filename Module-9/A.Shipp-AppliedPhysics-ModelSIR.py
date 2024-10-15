"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import matplotlib.pyplot as plt
import math as m
import scipy as sci
from scipy.integrate import odeint

####
# Variables & Constants
#===
MU = 0.1
BETA = 0.5

totalIdvs = 100
initI = 1
initR = 0
initS = totalIdvs-initI-initR
initY = [initS,initR,initI]
time = np.arange(0,100)

####
# Initializing Functions
#===
def infectionEqs(initConds,t,rtTransmission,rtRecovery,numPeople):
    fnctS,fnctR,fnctI = initConds
    dydt = [(-rtRecovery*fnctI*fnctS)/numPeople,rtTransmission*fnctI,((rtRecovery*fnctI*fnctS)/numPeople)-rtTransmission*fnctI]
    return dydt

#:Need to change dydt's order as well to change the SRI order -> SIR

####
# Work
#===
solution = odeint(infectionEqs,initY,time,args=(MU,BETA,totalIdvs))
valS = solution[:,0]
valI = solution[:,1]
valR = solution[:,2]


####
# Output Statements
#===
S=solution[:,0]
R=solution[:,1]
I=solution[:,2]
plt.figure()
plt.plot(time,valS,color='blue',label='Susceptible')
plt.plot(time,valI,color='black',label='Removed')
plt.plot(time,valR,color='red',label='Infected')
plt.grid()
plt.legend()
plt.xlabel('Time Elapsed (days)')
plt.ylabel('Polulation Groups')
plt.show()


"""
Base Eqs:
I(t) = # Infected at t
S(T) = # Susceptible at t
R(t) = # Removed at t
N = S(t) + I(t) + R(t)

Parameters:
N: Total # of persons (alive & dead)
beta = Transmission Rate
Mu = 1/T, aka Recovery Rate (inverse of the duration of illness)

D.E.'s: 
1) dS(t) = -(beta)S(t)I(t)
    dt           N
2) dR(t) = (mu)I(t)
    dt
3) dI(t) = (beta)S(t)I(t) - (mu)I(t)
    dt           N

Functions:
- Main function is scipy's odeint function
    - It requires a function that returns as many derivatives as there are unknowns (functions)
- Define a function with the derivatives
    - Y: Array of unkowns Y=(S,I,R)
    - t: Variable of integration
    - mu,beta,N: parameters


##################
#::Example Code::#

import matplotlib as plt

def infection(Y,t,mu,beta,N):
    S,R,I=Y #unpacks the array of unkowns
    dydt=[ -beta*I*S/N, mu*I, beta*I*S/N-mu*I ]
    return dydt

mu=0.1
beta=0.5
N=100

#There can't be a solution without initial conditions
I0=1
R0=0
S0=N-I0-R0

#Now pack the initial conditions (use the same order as they will be unpacked in "infection")
Y0=[S0,R0,I0]
t=np.arange(0,100)
#print(t)       #:Gives list of integers 0 through 99

solution=odeint(infection,Y0,t,args=(mu,beta,N))
print(solution)

# plot solutions as a function of time
S=solution[:,0]
R=solution[:,1]
I=solution[:,2]
plt.figure()
plt.plot(t,S,color='blue',label='S')
plt.plot(t,R,color='black',label='R')
plt.plot(t,I,color='red',label='I')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Infected')
plt.show()
"""
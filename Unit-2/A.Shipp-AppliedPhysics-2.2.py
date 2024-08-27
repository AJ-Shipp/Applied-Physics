"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Imports
#===
import math as m
import numpy as np

####
# Constants
#===
x = float()
y = float()

####
# Initializing Functions
#===
def deg2rad(angle):
    radians = angle * 2*np.pi / 360
    return radians

def conversions(radius,angle):
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    return x,y

####
# Work
#===
r = float(input("What is the radius in meters? "))
theta = deg2rad(float(input("What is the angle in degrees? ")))
x,y = conversions(r,theta)

####
# Output Statements
#===
print("Your inputs of a radius of %.1f meters and an angle equal to %.1f radians " 
      "is %.2f meters in the x direction and %.2f meters in the y-direction"
      %(r,theta,x,y))
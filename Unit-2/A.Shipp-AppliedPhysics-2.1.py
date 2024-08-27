"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Constants
#===
g = 9.81 #[m/s]

####
# Initializing Functions
#===
def calcDistFall(t,y):
    output = float()

    if t <= 0:
        print("That's not a proper input, please try again.")
        exit()
    elif g*t**2 > y:
        dist = y
    else: 
        dist = g*t**2
    return dist

####
# Prompts the user to input the time, in seconds, the ball has been falling for. Then what altitude, in meters, 
#  that the ball started at.
# Then the calculation function is called and distFall is set to the corresponding fall height. 
#===
time = float(input("Hello, how many seconds has the ball been falling for? "))
height = float(input("Great, now what altitude, in meters, did the ball begin at? "))
distFall = calcDistFall(time,height)

####
# Output statement
#===
print("The ball fell %.2f meters in %.2f seconds"%(distFall,time))
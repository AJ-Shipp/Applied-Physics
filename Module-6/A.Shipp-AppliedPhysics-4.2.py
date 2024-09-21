"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np

####
# Variables & Constants
#===
rowFirst = int()
columnFirst = int()
rowSecond = int()
columnSecond = int()
tryTranspose = bool()
passAllow = False

####
# Initializing Functions
#===
def checkDimensions(r1,d1,r2,d2):
    canPass = False
    tryT = False
    tryTranspose = False
    if d1 == r2:
        canPass = True
    if d1 != r2 and d2 == r1:
        print(
            'The matrices cannot be multiplied like this, but using the transpose of the second matrix would work.')
        tryT = int(input('Would you like to do this instead? If so, please enter 1, if not enter 0. '))
        if tryT == 1:
            canPass = True
            tryTranspose = True
    else:
        print("These matrices cannot be multiplied by one another.")
    return canPass, tryTranspose

def mtrxMult(matrix1,matrix2,methodNum):
    mtrxOut = []
    timer = time.time()
    if methodNum == 1:
        mtrxOut = matrix1 @ matrix2
    if methodNum == 2:
        mtrxOut = np.dot(matrix1,matrix2)
    if methodNum == 3:
        mtrxOut = np.matmul(matrix1,matrix2)
    if methodNum == 4:
        #:Create my own
        mtrxOut = None
    
    return mtrxOut


####
# Work
#===
"""
Intaking matrix dimensions
"""
while passAllow == False:
    rowFirst,columnFirst = input('Enter the numbers of rows and columns for matrix one with a space between the two numbers: ').split()
    rowSecond,columnSecond = input('Now, enter the numbers of rows and columns for matrix two with a space between the two numbers: ').split()
    
    passAllow,tryTranspose = checkDimensions(rowFirst,columnFirst,rowSecond,columnSecond)
    
    m1 = np.random.rand(int(rowFirst),int(columnFirst))
    m2 = np.random.rand(int(rowSecond),int(columnSecond))

"""
Finding the multiplication matrix using each separate method
"""
if tryTranspose == False:
    mtrxA,mtrxB = m1,m2
    mtrxMult(mtrxA,mtrxB,1)
elif tryTranspose == True:
    mtrxA,mtrxB = m2,m1
    mtrxMult()


####
# Output Statements
#===
print(m1,'\n\n',m2)



"""
- Use the .shape field to know the dimensions of a matrix (.shape)
- "For fun" find the transpose of a matrix (.T)
- Look up using input() but saving the data as an integer rather than a string
"""
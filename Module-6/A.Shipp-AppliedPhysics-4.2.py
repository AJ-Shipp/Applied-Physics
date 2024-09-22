"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Packages
#===
import numpy as np
import time

####
# Variables & Constants
#===
"""
rowFirst = Placeholder for the user's first matrix input's row size
columnFirst = Placeholder for the user's first matrix input's column size
rowSecond = Placeholder for the user's second matrix input's row size
columnSecond = Placeholder for the user's second matrix input's column size
tryTranspose = Boolean for attempting the matrix multiplication with a transpose, where needed
passAllow = Boolean to exit the while-loop
timeDelta = Reusable placeholder to find the calculation time
"""
rowFirst = int()
columnFirst = int()
rowSecond = int()
columnSecond = int()
tryTranspose = bool()
passAllow = False
timeDelta = int()

####
# Initializing Functions
#===
def checkDimensions(r1,d1,r2,d2):
    canPass = False
    tryT = False
    tryTranspose = False
    if d1 == r2:
        canPass = True
    elif d1 != r2 and d1 == d2:
        print(
            'The matrices cannot be multiplied like this, but using the transpose of the second matrix would work.')
        tryT = int(input('Would you like to do this instead? If so, please enter 1, if not enter 0. '))
        if tryT == 1:
            canPass = True
            tryTranspose = True
    elif d1 != r2 and d2 != r1:
        print("These matrices cannot be multiplied by one another.")
    return canPass, tryTranspose

def mtrxMult(matrix1,matrix2,methodNum):
    timeIn = time.time_ns()
    if methodNum == 1:
        #:Using numpy's @ feature
        mtrxOut = matrix1 @ matrix2
    if methodNum == 2:
        #:Using numpy's dot feature
        mtrxOut = np.dot(matrix1,matrix2)
    if methodNum == 3:
        #:Using numpy's matmul feature
        mtrxOut = np.matmul(matrix1,matrix2)
    if methodNum == 4:
        #:Create my own
        w1 = len(matrix1)
        l1 = len(matrix1[0])
        w2 = len(matrix2)
        l2 = len(matrix2[0])
        mtrxOut = np.zeros([w1,l2],float)

        for r in range(w1):
            for c in range(l2):
                for f in range(w2):
                    mtrxOut[r][c] += matrix1[r][f] * matrix2[f][c]

    timeOut = time.time_ns() - timeIn
    return mtrxOut,timeOut


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
    use1,timeDelta1 = mtrxMult(mtrxA,mtrxB,1)
    use2,timeDelta2 = mtrxMult(mtrxA,mtrxB,2)
    use3,timeDelta3 = mtrxMult(mtrxA,mtrxB,3)
    use4,timeDelta4 = mtrxMult(mtrxA,mtrxB,4)
elif tryTranspose == True:
    mtrxA,mtrxB = m1,np.transpose(m2)
    use1,timeDelta1 = mtrxMult(mtrxA,mtrxB,1)
    use2,timeDelta2 = mtrxMult(mtrxA,mtrxB,2)
    use3,timeDelta3 = mtrxMult(mtrxA,mtrxB,3)
    use4,timeDelta4 = mtrxMult(mtrxA,mtrxB,4)


####
# Output Statements
#===
print("\n4 Different calculation methods were used in this program.")
print("""
Firstly, using numpy's "@" feature results in:\n{}, after {:e} seconds.\n\n
Then, using numpy's "dot" feature results in:\n{}, after {:e} seconds.\n\n
Next, using numpy's "matmul" feature results in:\n{}, after {:e} seconds.\n\n
Finally, using my own method results in:\n{}, after {:e} seconds.\n\n
""".format(use1,timeDelta1*1e-9,use2,timeDelta2*1e-9,use3,timeDelta3*1e-9,use4,timeDelta4*1e-9))
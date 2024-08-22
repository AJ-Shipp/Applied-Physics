"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Creates an array named "text" which contains the main needed string values to output "Hello World"
# Also creates an output string variable named "outputT", and an interation integer named "num"
#===
text = ["H", "e", "l", "l", "o", "W", "r", "l", "d"]
outputT = ""
num = 0

####
# Iterates through each of the array's elements with specific parameters for different sections:
#  When num is less than 5, the element in "text" that corresponds to num's current value is added to the end of outputT
#  When num is equal to 5, first a space is added to outputT to separate the two words, second the element corresponding 
#   to num's current value is added to outputT, and finally the index which corresponds to the position of the letter "o"
#   in the array is selected by "text.index" and is then used to add another letter "o" to the outputT variable
#  When num is greater than 5, the remaining elements in text are added to the outputT variable as well
# Then the num integers value is increased by one at the end of each loop iteration  
#===
for letter in text:
    if num < 5:
        outputT = outputT + str(text[num])
    elif num == 5:
        outputT = outputT + str(" ")
        outputT = outputT + str(text[num]) 
        outputT = outputT + str(text[text.index("o")])
    elif num > 5:
        outputT = outputT + str(text[num])
    num += 1

####
# The outputT variable is printed out in the terminal 
#===
print(outputT)

#In class notes
"""
print('hi')
print("hello")
# ============
a=5.6
b=7.78
c=a+b
print(c)
"""

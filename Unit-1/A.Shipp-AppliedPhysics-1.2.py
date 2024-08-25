"""
Code written by AJ Shipp
Applied Physics (PH306-01)
"""

####
# Creates variables for the two numerical inputs, then uses the "input" function and "int()" function to intake
#  two numbers from the user and automatically asigns them the integer variable type
# Then prints each number out into the console
# Finds the sum of the two numbers
#===
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print(num1,num2)
sum = num1 + num2

####
# A improved printing statement that uses both "%i" placeholders for the num1 and num2 variables, while also using
#  a "%f" placeholder which automatically converts the sum to a float value with the modification of ".0" meaning
#  only the whole integer is printed but not anything after the float's decimal place
#===
print("The sum of %i and %i is %.0f" %(num1,num2,sum))

"""
Self reference: 

%f = float placeholder
%s = string placeholder
%i = integer placeholder
"""
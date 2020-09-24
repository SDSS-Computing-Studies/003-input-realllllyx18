#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math

side1=input("Enter the side1")
side2=input("Enter the side2")

total=float(side1)**2+float(side2)**2

hypotenuse=float(math.sqrt(total))
hypotenuse=str(hypotenuse)

result=("Input sides of 5 and 7 should give hypotenuse of "+hypotenuse)
print(result)

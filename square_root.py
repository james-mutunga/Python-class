# This program calculates the square root of a number entered by the user.

# We start by importing the math module, which contains functions for mathematical operations.

import math

# We use the sqrt() function from the math module to calculate the square root of the number entered by the user.
# We use float to allow for decimal inputs, as the square root can be calculated for decimal numbers.

num = float(input("Enter a number: "))

result = math.sqrt(num)

# We then print the calculated square root to the user using the print()

print(result)
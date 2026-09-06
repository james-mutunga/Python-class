# The calculator program

# We start by picking two numbers and an operator from the user
# We use float (a data type that can hold decimal numbers) to allow for decimal inputs
# Why did I use input and not just float(Enter first number: )? Because input() is a function that takes user input as a string, and we need to convert it to a float for calculations.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# The calculator logic

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    
    if num2 != 0:
        result = num1 / num2

    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
    
print("The result is: ", result) # This line prints the result of the calculation
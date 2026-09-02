# the calculator program

num1 = float(input("Enter first number: ")) # we use float to allow decimal numbers
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ") 

# the calculator logic

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
print("The result is: ", result) # this line prints the result of the calculation
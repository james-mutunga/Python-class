# This program converts Celsius to Fahrenheit

# We start by asking the user to input a temperature in Celsius
# We use float to allow for decimal inputs, as temperatures can be in decimal form.
# We use input() to take user input as a string, and then convert it to a float for calculations.

celsius = float(input("Enter temperature in Celsius: "))

# The formula to convert Celsius to Fahrenheit is: (Celsius * 9/5) + 32

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
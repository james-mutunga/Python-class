# This program calculates gross pay
# We start by asking the user to input the number of hours worked and the hourly rate.
# We use float to allow for decimal inputs, as hours and rates can be in decimal form.
# We use input() to take user input as a string, and then convert it to a float for calculations.

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# The formula to calculate gross pay is: hours * rate

pay = hours * rate

# Finally, we print the calculated gross pay to the user.
# We use print() to display the result, and we include a descriptive message for clarity.

print("Pay:", pay)

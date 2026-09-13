num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('Error: You cannot devide a number by 0!')
    else:
      print(num1 / num2)
else: 
    print('Error: Please enter (+, -, *, /)')
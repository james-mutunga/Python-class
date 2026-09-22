# Only 3 possible outcomes. Correct, Too High and Too Low.

import random

correct_number = random.randint(1, 100)
print(correct_number)

user_input = int(input("Enter a number: "))

while True:
    if user_input > correct_number:
        print("Too High! Try Again.")
        break
    elif user_input < correct_number:
        print("Too Low! Try Again.")
        break

    
# I started by storing each of my data (questions, choices and answer) in lists to allow for subsetting and indexing

questions = [
    {"q": "What is the capital of France?"},
    {"q": "Which planet is known as the Red Planet?"},
    {"q": "What is the largest mammal in the world?"}
]

choices = [
    {"A": "Paris", "B": "London", "C": "Berlin", "D": "Madrid"},
    {"A": "Mars", "B": "Venus", "C": "Jupiter", "D": "Saturn"},
    {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Hippopotamus"}
]

answer = ["A", "A", "B"]

score = 0

# QUESTION 1 SYNTAX

# This allows us to display the question of with index 0 of my questions list
print(questions[0]["q"])

# Here I included the input() in my try and except
try:
# user_answer will allow the user to input either of the choices displayed
  user_answer = input("A. Paris, B. London, C. Berlin, D. Madrid: ")
# user_choice will allow us to trigger the look up for other values such as "Z" or "zzz" (Not sure about this?)
  user_choice = choices[0][user_answer]
except KeyError:
  print("Error: Please enter (A, B, C or D)")
else:
    if user_answer == answer[0]:
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect!")

# QUESTION 2
print(questions[1]["q"])
try:
  user_answer = input("A. Mars, B. Venus, C. Jupiter, D. Saturn: ")
  user_choice = choices[1][user_answer]
except KeyError:
  print("Error: Please enter (A, B, C or D)")
else:
    if user_answer == answer[1]:
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect!")

# QUESTION 3
print(questions[2]["q"])
try:
  user_answer = input("A. Elephant, B. Blue Whale, C. Giraffe, D. Hippopotamus: ")
  user_choice = choices[2][user_answer]
except KeyError:
  print("Error: Please enter (A, B, C or D)")
else:
    if user_answer == answer[2]:
      print("Correct!")
      score = score + 1
    else:
      print("Incorrect!")

print(f"Your score is {score}/3")

# This is our score logic
if score == 3:
  print("Well done!")
elif score >= 2:
  print("Not bad.")
else:
  print("Better luck next time")
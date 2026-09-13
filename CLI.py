# Questions

# What is the capital city of France?
# Which planet is known as the Red Planet?
# What is the largest mammal in the world?

# Choices

# A. Paris B. London C. Berlin D. Madrid
# A. Mars B. Venus C. Jupiter, D. Saturn
# A. Elephant B. Blue Whale C. Giraffe D. Hippopotamus

# Correct Answers

# A
# A
# B

import random

# This is my quiz_data that will store 3 dictionaries for 3 different questons
quiz_data = [
    # dictionary for question 1 with its choices and correct answers
    {
        # question[0]
"question": "What is the capital city of France?",
        # choice[0]
"choice": {"A":"Paris", "B":"London", "C":"Berlin", "D":"Madrid"},
        # answer[0]
"answer": "A"
    },
        # dictionary for question 2 with its choices and correct answers
    {
        # question[1]
"question": "Which planet is known as the Red Planet?",
        # choice[1]
"choice": {"A":"Mars", "B":"Venus", "C":"Jupiter", "D":"Saturn"},
        # answer[1]
"answer": "A"
    },
        # dictionary for question 3 with its choices and correct answers
    {
        # question[2]
"question": "What is the largest mammal in the world?",
        # choice[2]
"choice": {"A":"Elephant", "B":"Blue Whale", "C":"Giraffe", "D": "Hippopotamus"},
        # answer[2]
"answer": "B"
    }
]

total = len(quiz_data)
score = 0
random.shuffle(quiz_data)

for quiz_data_index in range(total):
    question = quiz_data[quiz_data_index]
    print(f"\nQuestion {quiz_data_index + 1}/{total} : {question['question']}")

    for key, choice in question["choice"].items():
        print(f"{key}.{choice}")

    user_answer = input("\nYour Answer (A, B, C or D): ").upper().strip()

    while user_answer not in question["choice"]:
       print("Invalid input. Please enter A, B, C or D.")
       user_answer = input("\nYour Answer (A, B, C or D): ").upper().strip()

    correct_answer = question['answer']

    if user_answer == correct_answer:
     print("Correct Answer!")
     score +=1
    else:
     print("Wrong Answer.")

print(f"Your Score is {score}/{total}")
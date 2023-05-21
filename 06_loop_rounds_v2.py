"""Component 4 - loop rounds v2
Based on v1 but also calculates your final score and gives feedback
"""


import random

print("This quiz will test your knowledge of Maori numbers")


# List for easy difficulty
easy_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"],
                ["rima", "5"], ["ono", "6"], ["whitu", "7"], ["waru", "8"],
                ["iwa", "9"], ["tekau", "10"]]


# List for hard difficulty
hard_numbers = [["tekau ma tahi ", "11"], ["tekau ma rua", "12"],
                ["tekau ma toru", "13"], ["tekau ma wha", "14"],
                ["tekau ma rima", "15"], ["tekau ma ono", "16"],
                ["tekau ma whitu", "17"], ["tekau ma waru", "18"],
                ["tekau ma iwa", "19"], ["rua tekau", "20"]]
score = 0


# Main Routine
level = input("What difficulty level would you like to play at?"
              " (1 for easy), (2 for hard) ")
if level == "2":
    print(f"You are playing at hard difficulty")
    level = hard_numbers  # Sets difficulty to hard
else:
    print(f"You are playing at easy difficulty")
    level = easy_numbers  # Sets difficulty to easy

random.shuffle(level)  # Makes sure that each number is only shown once


# Checking if answer is correct
for i in level:
    # Selecting a random question
    answer = input("Enter the number for {}: ".format(i[0]))
    # If answer is answered correctly add a point to the score
    if answer == i[1]:
        print("well done correct")
        score += 1
    # If answer is incorrect keep score the same
    else:
        print("incorrect")
        score += 0


# Gives the final score as well as feedback
print(f"Your final score is {score}/10")
if score < 3:
    print("Your knowledge of Maori numbers is quite poor")
elif 3 <= score <= 7:
    print("Your knowledge of Maori numbers is alright")
elif 8 <= score <= 9:
    print("Well done you scored highly")
else:
    print("You got a perfect score!")

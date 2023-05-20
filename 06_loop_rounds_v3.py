"""Component 4 - question_generator v3
Turns v2 into a function and includes the question number
"""


import random

print("This quiz will test your knowledge of Maori numbers")


def generate_question(score):
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

    level = input("What difficulty level would you like to play at?"
                  " (1 for easy), (2 for hard) ")
    if level == "2":
        print(f"You are playing at hard difficulty")
        level = hard_numbers  # Sets difficulty to hard
    else:
        print(f"You are playing at easy difficulty")
        level = easy_numbers  # Sets difficulty to easy

    random.shuffle(level)  # Makes sure that each number is only shown once
    question_number = 1

    for i in level:
        print(f"Question {question_number}")
        answer = input("Enter the number for {}: ".format(i[0]))
        question_number += 1
        if answer == i[1]:
            print("well done correct")
            score += 1
        else:
            print("incorrect")
            score += 0
    return score


# Main Routine
starting_score = 0
final_score = generate_question(starting_score)

# Shows the final score of the quiz
print(f"Your final score is {final_score}/10 ")

# Gives feedback on final score
if final_score < 3:
    print("Your knowledge of Maori numbers is quite poor")
elif 3 <= final_score <= 7:
    print("Your knowledge of Maori numbers is alright")
elif 8 <= final_score <= 9:
    print("Well done you scored highly")
else:
    print("You got a perfect score!")

"""Maori Quiz base component v3
Instructions and text decoration added"""

import random


# function to format into text output (based off lucky unicorn)
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Yes no checker function (based off lucky unicorn)
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "Display Instructions"
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - Show error
        else:
            print("Please answer 'yes' or 'no'")


# Function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("First, choose a difficulty level to play at. ")
    print()
    print("\tDifficulty level 1 is numbers 1-10")
    print("\tDifficulty level 2 is numbers 11-20")
    print()
    print("Each question adds 1 point to your score total. Your final score "
          "will be given at the end out of 10.")
    print("Feedback will be given on your final score. See if you can get a "
          "perfect score!\n")
    print("-" * 100)


# Number Checking function (based off lucky unicorn)
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number; either {} or {}\n".format(low, high)

    # Keep asking until a valid amount (1 or 2) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# random question generator
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

    if difficulty_level == 2:
        level = hard_numbers  # Sets difficulty to hard
    else:
        level = easy_numbers  # Sets difficulty to easy

    random.shuffle(level)  # Makes sure that each number is only shown once
    question_number = 1

    for i in level:
        print(formatter("|", f"Question {question_number}"))
        print()
        # Selecting a random question
        answer = input("Enter the number for {}: ".format(i[0]))
        question_number += 1
        # If answer is answered correctly add a point to the score
        if answer == i[1]:
            print(formatter("!", "well done correct"))
            print()
            print("-" * 50)
            score += 1
        # If answer is incorrect keep score the same
        else:
            print(formatter("x", "incorrect"))
            print()
            print("-" * 50)
            score += 0
    return score


# Main routine goes here.....
print(formatter("-", "Welcome to the Maori Quiz"))
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Ask what difficulty level they want to play at
difficulty_level = num_check("What difficulty level would you like to play at?"
                             " (1 for easy), (2 for hard) ", 1, 2)
if difficulty_level == 2:
    print(f"You are playing at hard difficulty")
    print()
else:
    print(f"You are playing at easy difficulty")
    print()

starting_score = 0
final_score = generate_question(starting_score)

# Show final score
print(f"Your final score is {final_score}/10 ")

# Give feedback on final score
if final_score < 3:
    print("Your knowledge of Maori numbers is quite poor")
elif 3 <= final_score <= 7:
    print("Your knowledge of Maori numbers is alright")
elif 8 <= final_score <= 9:
    print("Well done you scored highly")
else:
    print("You got a perfect score!")

print("Thanks for playing")
print()
print(formatter("*", "Goodbye"))

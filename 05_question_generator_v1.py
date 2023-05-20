"""Component 3 - question_generator v1
Generates questions in a random order
"""


import random


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


# Testing loop for 10 questions from list 1
for item in range(10):
    easy_number = random.choice(easy_numbers)

    # can wrap output making it easier to screenshot
    print(easy_number, end='\t')

# Testing loop for 10 questions from list 2
print()
for item in range(10):
    hard_number = random.choice(hard_numbers)
    print(hard_number, end='\t')

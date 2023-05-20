""" Component 3 - question_generator v2
Generates numbers in a random order without repeats (each number
only appears once) """


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


# Making sure each number from easy_number list appears once only
random.shuffle(easy_numbers)
for item in range(1):
    print(easy_numbers)

# Making sure each number from hard_number list appears once only
random.shuffle(hard_numbers)
print()
for item in range(1):
    print(hard_numbers)

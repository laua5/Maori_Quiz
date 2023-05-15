""" Component 3 - question generator v3
Sets difficulty level to hard and prints all ten numbers (randomly)
 on a separate line as well as the question number"""


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

random.shuffle(hard_numbers)  # Shuffles the list so that there are no repeats
random.shuffle(easy_numbers)  # Shuffles the list so that there are no repeats


# Sets list to hard_numbers
print(f"Number 1:{(hard_numbers[1])} ")
print(f"Number 2:{(hard_numbers[2])} ")
print(f"Number 3:{(hard_numbers[3])} ")
print(f"Number 4:{(hard_numbers[4])} ")
print(f"Number 5:{(hard_numbers[5])} ")
print(f"Number 6:{(hard_numbers[6])} ")
print(f"Number 7:{(hard_numbers[7])} ")
print(f"Number 8:{(hard_numbers[8])} ")
print(f"Number 9:{(hard_numbers[9])} ")
print(f"Number 10:{(hard_numbers[0])} ")

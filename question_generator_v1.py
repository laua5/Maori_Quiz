import random

print("This quiz will test your knowledge of Maori numbers")

easy_numbers = [["tahi", "1"], ["rua", "2"], ["toru", "3"], ["wha", "4"],
                ["rima", "5"], ["ono", "6"], ["whitu", "4"], ["waru", "8"],
                ["iwa", "9"], ["tekau", "10"]]

hard_numbers = [["tekau ma tahi ", "11"], ["tekau ma rua", "12"],
                ["tekau ma toru", "13"], ["tekau ma wha", "14"],
                ["tekau ma rima", "15"], ["tekau ma ono", "16"],
                ["tekau ma whitu", "17"], ["tekau ma waru", "18"],
                ["tekau ma iwa", "19"], ["rua tekau", "20"]]


# Main Routine
user_balance = input("What difficulty level would you like to play at?"
                     " (1 for easy), (2 for hard) ")
if user_balance == "2":
    print(f"You are playing at hard difficulty")
    user_balance = hard_numbers
else:
    print(f"You are playing at easy difficulty")
    user_balance = easy_numbers

random.shuffle(user_balance)

for i in user_balance:
    answer = input("Enter the english word for {}: ".format(i[0]))
    if answer == i[1]:
        print("well done correct")
    else:
        print("incorrect")

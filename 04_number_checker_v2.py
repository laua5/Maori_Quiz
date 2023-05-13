""" Component 2 (how much) v2
Use try/accept and pull error message out of the loop"""

error = "Please enter a number either 1 and 2\n"
valid = False

# Keep asking until a valid amount (1 or 2) is entered
while not valid:
    try:
        # ask for difficulty level
        difficulty_level = int(input("What difficulty level would you like to "
                                     "play at? (1 for easy, 2 for hard) :"))

        # Check if the amount is too high/low
        if 0 < difficulty_level <= 2:
            if difficulty_level == 2:
                print("You are playing at hard difficulty")
            else:
                print("You are playing at easy difficulty")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)

""" Component 2 - difficulty level
Asks user which difficulty level they which to play at ( 1 for easy,
 2 for difficult) If it is a valid input their input will be their difficulty
 level
"""

difficulty_level = int(input("What difficulty level would you like to play at?"
                             "(1 for easy, 2 for hard): "))


# Keep asking until a valid input is entered
while not 1 <= difficulty_level <= 2:
    print("Try again. Please enter either 1 for easy or 2 for hard "
          "difficulty.")
    # Ask for the input again
    difficulty_level = int(input("What difficulty level would you like to "
                                 "play at? "))

# Main routine
if difficulty_level == 1:
    print("You are playing at easy difficulty")
else:
    print(print(f"You are playing at hard difficulty"))

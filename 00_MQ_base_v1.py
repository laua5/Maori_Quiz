"""Maori Quiz base component
Components are added here after they have been tested and created"""


# Functions go here
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
    print("The rules of the game will go here")
    print()


# Number Checking function
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


# Main routine goes here.....
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# Ask user what difficulty level they would like to play with
difficulty_level = num_check("What difficulty level would you like to play at?"
                             " (1 for easy), (2 for hard) ", 1, 2)
if difficulty_level == 2:
    print(f"You are playing at hard difficulty")
else:
    print(f"You are playing at easy difficulty")

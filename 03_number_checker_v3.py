""" Component 2 (difficulty level)
Changing v2 into a function
Also needed to change user_balance to the more generic variable name 'response'
and to change the condition and position of the number comparison into a loop
to make the function recyclable"""


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number; either {} or {}\n".format(low, high)

    # Keep asking until a valid amount (1-10) is entered
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


# Main Routine
difficulty_level = num_check("What difficulty level would you like to play at?"
                             " (1 for easy), (2 for hard) ", 1, 2)
if difficulty_level == 2:
    print(f"You are playing at hard difficulty")
else:
    print(f"You are playing at easy difficulty")

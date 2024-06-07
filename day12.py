import random

# used r so that python will interpret it as raw string
logo = r""" 

   _____                       _   _            _   _                 _               
  / ____|                     | | | |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                      
"""
print(logo)
print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

to_guess = random.randint(1, 100) # random number between 1 - 100

# print(f"psst, the answer is {to_guess}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

chances = 0

while True:  # will ask for input if recent input is incorrect

    if level.lower() == 'easy':
        chances = 10
        print(f"You have {chances} chances")
        break
    elif level.lower() == 'hard':
        chances = 5
        print(f"You have {chances} chances")
        break
    else:
        print("Incorrect Input \n")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")

print()

#  Checks if input is integer, if not prompt input again
def get_integer_input(prompt):
    """
       Prompt the user for input until a valid integer is entered.

       Args:
           prompt (str): The message displayed to the user when asking for input.

       Returns:
           int: The valid integer entered by the user.
       """
    while True:
        user_input = input(prompt)
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            return int(user_input)
        else:
            print("Invalid input. Please enter an integer.")


# Get initial guess
user_guess = get_integer_input("Make a guess: ")

while  user_guess != to_guess and chances != 1:

    if user_guess < to_guess:
        chances -= 1
        print("Guess too low, try again.")
        print(f"You have {chances} attemps remaining. \n")
        user_guess = get_integer_input("Make a guess: ")
    else:
        chances -= 1
        print("Guess too high, try again.")
        print(f"You have {chances} attemps remaining. \n")
        user_guess = get_integer_input("Make a guess: ")

print()
 # Check if user WON or NOT
if user_guess == to_guess:
    print("GOOD GAME")
    print(f"You guessed {to_guess}")
else:
    print("GAME OVER")
    print(f"The hidden game is: {to_guess}!")





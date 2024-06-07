# HIGHER or LOWER project (but instagram)

import day14data
import random

data_list = day14data.data
score = 0


# FUNCTIONS
def randomizer():
    return random.randint(1, len(data_list) - 1)


def description(data):  # function that prints data of X dictionary
    name = data["name"]
    desc = data["description"]
    country = data["country"]
    return f"{name}, a {desc}, {country}."


def startGame():
    global score
    indexA = randomizer()
    indexB = randomizer()

    personaA = None
    personaB = None

    # to check in case both have the same index (comparison won't work if values are the same)
    if indexA == indexB:
        indexB = randomizer()
        personaA = data_list[indexA]
        personaB = data_list[indexB]
    else:
        personaA = data_list[indexA]
        personaB = data_list[indexB]

    print("Compare A: ", description(personaA))
    print("VS")
    print("Against B: ", description(personaB))

    user_guess = input("Who has more followers? Type 'A or 'B': ").lower()

    # user input checker (only accepts 'A' and 'B' INPUT)
    while user_guess != 'a' and user_guess != 'b':
        user_guess = input("Who has more followers? Type 'A or 'B': ").lower()

    if user_guess == 'a':
        if personaA["follower_count"] > personaB["follower_count"]:
            # print(personaA["follower_count"], personaB["follower_count"])
            print("corique ka dai")
            score += 1
            print(f"Current score: {score}\n")
        else:
            # print(personaA["follower_count"], personaB["follower_count"])
            print("NGEK")
            print(f"Your final score: {score}\n")
            exit()  # exits code, acts as break (but not the same behavior)

    else:
        if personaB["follower_count"] > personaA["follower_count"]:
            # print(personaA["follower_count"], personaB["follower_count"])
            print("corique ka dai")
            score += 1
            print(f"Current score: {score}\n")
        else:
            # print(personaA["follower_count"], personaB["follower_count"])
            print("NGEK")
            print(f"Your final score: {score}\n")
            exit()


while True:  # just continue playing if user is correct
    startGame()
# loop over the list of dictionaries for the followers value
# compare it to check if user guess is right
# make a score counter

# then, if user is right continue playing otherwise game over and total score

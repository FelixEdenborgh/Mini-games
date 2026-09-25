import random

"""
Number Guessing Game
Spara ett numersikt värde som korrekt svar i variabel.
Spelaren ska via konsolen försöka gissa värdet på korrekt svar.
För varje gissning får spelaren veta om gissningen är - för lågt, för högt eller korrekt.
Om gissningen inte är korrekt fortsätter spelet
Om gissningen är korrekt avslutas spelet och spelaren informeras om hur många gissningar det tog att få korrekt svar
"""

"""
a. Utvecka med nivåer
För vardera spel gör om variabeln för korrekt svar till en sekvens.
I början av varje spel lägg till en meny där man väljer vilken nivå man vill spela.
"""

def play():
    number_of_guesses = 0
    easy = random.randint(1, 9)
    medium = random.randint(1, 20)
    hard = random.randint(1, 100)
    number = 0
    win = 0

    print("Welcome to this guessing game. \n to win enter the right number")

    print("Enter which level you wanna play at: easy, medium and hard")
    level = input().lower()
    if level.isalpha():
        print(f"You have selected {level}")

        if level == "easy":
            number = easy
        elif level == "medium":
            number = medium
        elif level == "hard":
            number = hard
        else:
            print("You have not choicen right so congratulations lets start at Level Hard")
            number = hard

    else:
        print("You have not choicen right so congratulations lets start at Level Hard")

    while(win != 1):
        try:
            user_guess = int(input("choice your number: "))
        except ValueError:
            print("It most be a number")
            continue
        number_of_guesses += 1

        if user_guess == number:
            print("You win!")
            print(f"You made {number_of_guesses} guesses to win \n Congratulations!!! \n The number was {number}")
            win = 1
            break

        elif user_guess < number:
            print("To low!")

        elif user_guess > number:
            print("To High!")

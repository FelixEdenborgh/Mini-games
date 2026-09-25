import Guessing_Game, Hangman


"""
b. Utveckla med hub
Skapa en meny där man väljer vilket spel man vill spela
"""


print("Welcome to this years game Hub, Which game do you wanna play? \n 1. GuessingGame \n 2. Hangman")

user_choice = input().lower()

if user_choice.isalpha():
    if user_choice == "guessinggame":
        Guessing_Game.play()

    elif user_choice == "hangman":
        Hangman.Play()

    else:
        print("You dont wanna play?")
else:
    print("Thats not a word")
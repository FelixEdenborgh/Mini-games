import random


"""
Hangman
Spara ett textvärde som korrekt svar i en variabel
Spelaren ska via konsolen försöka gissa en textkaraktärer som finns i korrekt svar.
För varje gissning får spelaren veta om gissningen - inte ingår eller ingår i korrekt svar.
För varje gissning får spelaren veta vilka fel gissningar och rätt gissningar som tidigare gjorts.
För varje gissning får spelaren veta hur nära de är att förlora.
För varje fel svar kommer spelaren närmare att förlora.
Om alla unika textkaraktärer som finns i korrekt svar är gissade, får spelaren veta att de vunnit och spelet avslutas.
Om nivån för att förlora uppnås, får spelaren veta att de förlorat och spelet avslutas.
"""

"""
a. Utvecka med nivåer
För vardera spel gör om variabeln för korrekt svar till en sekvens.
I början av varje spel lägg till en meny där man väljer vilken nivå man vill spela.
"""

def Play():
    easy_words = ["milk", "phone", "router"]
    medium_words = ["cookie", "python"]
    hard_words = ["programming", "development"]
    charinputs = []

    Hangman_rules_of_max_choices = 9
    win = 0

    print("Welcome to Hangman game! \n here you need to choice a char: 'letter' \n and we will check if its inside the word. \n max 8 quesses or the man will be Hanged!")


    print("Choice level you wanna play at easy, medium and hard")
    level = input().lower()
    if level.isalpha():
        print(f"You have choiced the difficulty of {level} lets PLAY!")
        if level == "easy":
            random_word = random.choice(easy_words)
        elif level == "medium":
            random_word = random.choice(medium_words)
        elif level == "hard":
            random_word = random.choice(hard_words)
        else:
            print("You never desided, so lets start at hardest level WHOHOO!!!")
            random_word = random.choice(hard_words)

    while(win != 1):
        choice = input("Enter your char:").lower()

        if len(choice) == 1 and choice.isalpha():
            if choice in random_word:
                charinputs.append(choice)
                print(f"You guessed right {choice} are in the word")

                print("Your guessed characters: ")
                for char in charinputs:
                    if char in charinputs:
                        print(char, end=" ")
                    else:
                        print("_", end=" ")

                if all(char in charinputs for char in random_word):
                    print(f"\nYou won with \n {Hangman_rules_of_max_choices} Lives Left. \n Word was {random_word}")
                    win = 1
                    break

            elif Hangman_rules_of_max_choices == 1:
                print(f"You lost! word was {random_word}")
                win = 1
                break

            else:
                Hangman_rules_of_max_choices -= 1
                print(f"{choice} arent inside the word \n you have Lives {Hangman_rules_of_max_choices} left")
        else:
            print("Wright only 1 character")
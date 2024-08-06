import random
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    target = random.randint(1, 100)

    logo = """
    █████▀███████████████████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄█▄─██─▄█▄─▄▄─█─▄▄▄▄█─▄▄▄▄███─▄─▄─█─█─█▄─▄▄─███▄─▀█▄─▄█▄─██─▄█▄─▀█▀─▄█▄─▄─▀█▄─▄▄─█▄─▄▄▀█
    █─██▄─██─██─███─▄█▀█▄▄▄▄─█▄▄▄▄─█████─███─▄─██─▄█▀████─█▄▀─███─██─███─█▄█─███─▄─▀██─▄█▀██─▄─▄█
    ▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
    """
    print(logo)

    print("I have chosen a number between 1 and 100")
    print("Good Luck Guessing It :)")

    print("\nChoose Your Difficulty Level!")
    difficulty_level = input("Type e for Easy || Type h for Hard: ").lower()

    if difficulty_level == 'e':
        guesses = 10
    else:
        guesses = 5
    
    while guesses > 0:
        print(f"\nGuesses Left -> {guesses}")

        attempt = int(input("Input your Guess: "))

        if target == attempt:
            print("\nYou Won!")
            sys.exit()

        elif target > attempt:
            print("\nTry Higher!")

        elif target < attempt:
            print("\nTry Lower!")

        guesses -= 1
    
    print("You've run out of guesses! You lose.")
    print(f"\nThe number to guess was {target}")
    
    play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit: ").lower()
    if play_again == 'y':
        clear()
        play_game()
    else:
        print("Goodbye.")

play_game()

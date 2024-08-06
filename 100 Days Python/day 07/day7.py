import random

stages = [
    """
      +---+
      |   |
      O   |
     /|\\ |
     / \\ |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\ |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\ |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

logo3 = """
  _    _                     __  __             
 | |  | |                   |  \/  |            
 | |__| | __ _ _ __   __ _  | \  / | __ _ _ __  
 |  __  |/ _` | '_ \ / _` | | |\/| |/ _` | '_ \ 
 | |  | | (_| | | | | (_| | | |  | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, | |_|  |_|\__,_|_| |_|
                      __/ |                     
                     |___/                                          
"""


win_art = """
 __     __          __          ___       
 \ \   / /          \ \        / (_)      
  \ \_/ /__  _   _   \ \  /\  / / _ _ __  
   \   / _ \| | | |   \ \/  \/ / | | '_ \ 
    | | (_) | |_| |    \  /\  /  | | | | |
    |_|\___/ \__,_|     \/  \/   |_|_| |_|
"""

lose_art = """
 __     __           _                          
 \ \   / /          | |                         
  \ \_/ /__  _   _  | |     ___   ___  ___  ___ 
   \   / _ \| | | | | |    / _ \ / _ \/ __|/ _ \
    | | (_) | |_| | | |___| (_) | (_) \__ \  __/
    |_|\___/ \__,_| |______\___/ \___/|___/\___|
"""

word_list = ["python", "developer", "challenge", "hangman", "puzzle", "programming"]

def clear():
    print("\n" * 100)

def hangman_game():
    print(logo3)
    print("\nTo win, guess the word before the person is hung.\n")

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    display = ["_" for _ in range(word_length)]
    wrong_guesses = []
    correct_guesses = set() 

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear()

        if guess in correct_guesses or guess in wrong_guesses:
            print(f"You've already guessed '{guess}'. Try a different letter.")
        elif guess in chosen_word:
            correct_guesses.add(guess)
            for position in range(word_length):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            wrong_guesses.append(guess)
            lives -= 1
            print(f"'{guess}' is not in the word. You lose a life.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("\nGenius, genius, genius! You won!")
            print(win_art)
        elif lives == 0:
            end_of_game = True
            print(stages[lives])
            print("The man has been hung, you lose.")
            print(lose_art)
            print(f"\nThe word was '{chosen_word}'")

        if not end_of_game:
            print(stages[lives])
            if lives > 0 and guess not in display:
                print(f"Incorrect guesses: {', '.join(wrong_guesses)}")

hangman_game()

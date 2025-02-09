# This is our solution may not be the best one but it works



import random 

def get_word() -> str:
    """
    Return a random word from a list of words
    param: None
    return: str
    """
    word_list : list[str] = ['cat', 'dog', 'rabbit', 'hamster', 'goldfish', 'parrot', 'canary', 'duck', 'pigeon', 'python', 'spider', 'ferret', 'lizard', 'turtle', 'chinchilla', 'squirrel', 'gerbil', 'hedgehog', 'tarantula', 'scorpion']
    return random.choice(word_list) 

def display_hangman(lives : int) -> None:
    """
    Display the hangman based on the number of lives left
    param: int
    return: None
    """
    hangman_stages : list[str] = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    
    # Draw the hangman stage
    print(hangman_stages[6 - lives])

def get_guess(guessed_letters : list[str]) -> str:
    """
    Get a letter from the user and validate it
    param: list
    return: str
    """
    while True:  # Loop until a valid and not guessed before letter is entered
        letter : str = input('Choose a letter: ').lower()
        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single letter.")
        elif letter in guessed_letters:
            print("You've already guessed that letter!")
        else:
            return letter

def play_game() -> None:
    """
    Play the hangman game
    param: None
    return: None
    """
    word_to_guess : str = get_word()
    word_guessed : list[str] = ['_'] * len(word_to_guess)
    lives : int = 6
    guessed_letters : list[str] = list()

    while lives > 0 and '_' in word_guessed: # Loop until the player wins or loses
        display_hangman(lives)
        print(' '.join(word_guessed))
        print(f'Guessed letters: {", ".join(sorted(guessed_letters))}')
        
        letter : str = get_guess(guessed_letters)
        guessed_letters.add(letter)
        
        if letter in word_to_guess: # Change the letter_to_guess list to show the correct letter
            for i, char in enumerate(word_to_guess):
                if char == letter:
                    word_guessed[i] = letter
        else: # Decrease the lives if the letter is not in the word
            lives -= 1
            print(f'Incorrect! You have {lives} lives left.')

    display_hangman(lives)
    if lives == 0: # Check if the player lives are over
        print(f'You lost! The word was: {word_to_guess}')
    else:
        print(' '.join(word_guessed))
        print('You won! 🎉')

# Start the game
play_game()

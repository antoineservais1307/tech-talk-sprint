# Make this code as readable and understable as possible and make sur it works ;) 


def hangman():
    list = ['cat', 'dog', 'rabbit', 'hamster', 'goldfish', 'parrot', 'canary', 'duck', 'pigeon', 'python', 'spider', 'ferret', 'lizard', 'turtle', 'chinchilla', 'squirrel', 'gerbil', 'hedgehog', 'tarantula', 'scorpion']
    word_to_guess = random.choice(list)
    word_guessed = ['_'] * len(word_to_guess)
    x = 6
    guessed_letters = set()
    hangman_stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========" ,
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========" 
    ]
    while x > 0 and '_' in word_guessed:
        print(hangman_stages[6 - x])
        print(' '.join(word_guessed))
        print(f'Guessed letters: {", ".join(sorted(guessed_letters))}')
        y = input('Choose a letter: ').lower()
        if not y.isalpha() or len(y) != 1:
            print("Please enter a single letter.")
            continue
        if y in guessed_letters:
            print("You've already guessed that letter!")
            continue
        guessed_letters.add(y)
        if y in word_to_guess:
            for i, char in enumerate(word_to_guess):
                if char == y:
                    word_guessed[i] = y
        else:
            x -= 1
            print(f'Incorrect! You have {x} lives left.')
    print(hangman_stages[6 - x])
    if x == 0:
        print(f'You lost! The word was: {word_to_guess}')
    else:
        print(' '.join(word_guessed))
        print('You won! 🎉')
hangman()
import random

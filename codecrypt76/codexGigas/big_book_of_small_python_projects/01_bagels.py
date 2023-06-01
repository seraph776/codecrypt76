#!/usr/bin/env python3
"""
created: codecrypt76/05/21 10:31:36
@author: seraph★776
project: Big Book of Small Python Projects
metadoc: Bagels
"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100


def main():
    print(f"""Bagels, a deductive logic game
    
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
        - Pico    One digit is correct but in the wrong position.
        - Fermi   One digit is correct and in the right position.
        - Bagels  No digit is correct
    For example, if the secret number was 248 and your guess was 843, the clue would be Fermi Pico   
    """)

    while True:  # Main loop
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # They're correct, so break out of the loop.
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}.')

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')


def get_secret_num():
    """Return a string made up of NUM_DIGITS unique random digits"""
    numbers = list('0123456789')  # Create a list of digits 0 to 9
    random.shuffle(numbers)  # Shuffle them into random order

    # Get the first NUM_DIGIT digits in the list for the secret number:
    output = ''
    for i in range(NUM_DIGITS):
        output += str(numbers[i])
    return output


def get_clues(guess, secret_num):
    """Return a string with pico, fermi, bagels clue for guess and secret number pair"""
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There is no correct digit at all.
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away
        clues.sort()
        # Make a single string from the of list of clues:
        return ' '.join(clues)


if __name__ == '__main__':
    main()

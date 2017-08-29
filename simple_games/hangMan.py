import os
import random
import sys

# make a list of words
words = [
    'apple',
    'pizza',
    'lettuce',
    'car',
    'truck',
    'frisbee',
    'person',
    'banana',
    'tractor',
    'grass',
    'television',
    'instrument',
    'wizard',
    'knight',
    'ogre',
    'ocra',
    'elephant',
    'sloth',
    'dolphin',
    'light',
    'computer',
    'friend',
    'cowboy'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(badGuesses, goodGuesses, secretWord):
    clear()

    print('Strikes: {}/7'.format(len(badGuesses)))
    print('')

    for letter in badGuesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secretWord:
        if letter in goodGuesses:
            print(letter, end='')
        else:
            print('_', end='')

    print('')

def getGuess(badGuesses, goodGuesses):
    # get a guess
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter")
        elif guess in badGuesses or guess in goodGuesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    secretWord = random.choice(words)
    badGuesses = []
    goodGuesses = []

    while True:
        draw(badGuesses, goodGuesses, secretWord)
        guess = getGuess(badGuesses, goodGuesses)

        if guess in secretWord:
            goodGuesses.append(guess)
            found = True
            for letter in secretWord:
                if letter not in goodGuesses:
                    found = False
            if found:
                draw(badGuesses, goodGuesses, secretWord)
                print("You Win!")
                print("The secret word was {}!".format(secretWord))
                done = True
        else:
            badGuesses.append(guess)
            if len(badGuesses) == 7:
                draw(badGuesses, goodGuesses, secretWord)
                print("You lost!")
                print("The secret word was {}!".format(secretWord))
                done = True

        if done:
            playAgain = input("Play again? Y/n ").lower()
            if playAgain != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True

print("Welcome to Letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done)

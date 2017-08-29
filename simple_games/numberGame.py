import random


def game():
    userNum = None
    userResponse = None
    guesses = []
    # user selected number
    while userNum is None:
        try:
            userNum = int(input("Please enter a number for me to try and guess. "))
        except ValueError:
            print("Good try.  That's not a number.  Try again.")
        else:
            # computer tries a guess
            while len(guesses) < 5:
                if userResponse is None:
                    comGuess = random.randint(1, 10)
                elif userResponse.lower() == "too high":
                    comGuess = random.randint(1, (comGuess-1))
                else:
                    comGuess = random.randint((comGuess+1), 10)

                # computer tells user its guess
                # user says it's either right, too high, or too low
                userResponse = input("Try {}: Is your number {}? [Yep, Too High, Too Low] ".format((len(guesses) + 1), comGuess))
                if userResponse.lower() == 'yep':
                    print("I knew it all along.  Yippy for me!")
                    break
                else:
                    guesses.append(comGuess)
        playAgain = input("Do you want to play again? Y/n ")
        if playAgain.lower() != 'n':
            game()
        else:
            print("Bye!")


game()

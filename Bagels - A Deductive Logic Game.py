import random
Num_Digits = 3
Max_Guesses = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(Num_Digits))
    
    secretNum = getSecretNum()
    # print(f"Secret number: {secretNum}")
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(Max_Guesses))

    while True: # Main game loop
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(Max_Guesses))

        numGuess = 1
        while numGuess <= Max_Guesses:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != Num_Digits or not guess.isdecimal():
                print('Guess #{} '.format(numGuess))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuess += 1

            if guess == secretNum:
                break
            if numGuess > Max_Guesses:
                print('You ran out of guesses,')
                print('The answer was {}'.format(secretNum))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startwith('y'):
            break
    print('Thanks for playing')


def getSecretNum():
    """Return a string made up of Num_Digits unique random digits."""
    numbers = list("0123456789") # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffel them into random oredr

    # Getthe first Num)Digits in the list for the secret numbers:
    secretNum = ''
    for i in range(Num_Digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A corect digit in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit in the wrong place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of the srting clues.
        return ' '.join(clues)
    
# If the program is run (instead or imported), run the game:
if __name__ == '__main__':
    main()
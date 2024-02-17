#-----------------------------------------------------------------------------
# Name:  CCC '12 J4 - Big Bang Secrets (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------

# Takes the shift value as input
shiftValue = int(input())

# Takes the encoded word as input
encodedWord = input()

# Defines the English alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Initializes a list to store the decoded word
decodedWord = list(encodedWord)

# Iterates through each letter in the encoded word
for position in range(len(encodedWord)):
    # Calculate the position of the letter in the word
    letterPosition = position + 1
    # Calculate the shift for this letter
    shift = 3 * letterPosition + shiftValue

    # Finds the decoded letter using modular arithmetic
    decodedWord[position] = alphabet[(alphabet.index(encodedWord[position]) + len(alphabet) - shift) % len(alphabet)]

# Prints the decoded word
print(''.join(decodedWord))
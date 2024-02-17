#-----------------------------------------------------------------------------
# Name: CCC '22 J3 - Harp Tuning (main.py)
# Author:      Aryan Mittal
# Created:     16-Feb-2024
# Updated:     16-Feb-2024
#---------------------------------------------------------------------------

inputSequence = str(input())

uppercaseLetters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
isNumberPresent = False
numberToPrint = 0

for char in inputSequence:
    if char in numbers:
        isNumberPresent = True
        print(char, end="")

    elif char not in numbers:
        if isNumberPresent:
            print()
            isNumberPresent = False

        if char == "+":
            print(" tighten ", end="")
            isNumberPresent = False

        elif char == "-":
            print(" loosen ", end="")
            isNumberPresent = False

        elif char in uppercaseLetters:
            print(char, end="")
            isNumberPresent = False
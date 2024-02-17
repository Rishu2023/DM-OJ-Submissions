#-----------------------------------------------------------------------------
# Name: CCC '19 S1 - Flipper (main.py)
# Author:      Aryan Mittal
# Created:     16-Feb-2024
# Updated:     16-Feb-2024
#---------------------------------------------------------------------------
# Reads the input sequence representing the flips
flipSequence = input()

# Initializes the initial grid with four of the different numbers
initialGrid = [1, 2, 3, 4]

# Iterates over each flip in the sequence
for flip in flipSequence:
    if flip == "H":
        # Performs a horizontal flip on the grid
        initialGrid[0], initialGrid[1], initialGrid[2], initialGrid[3] = initialGrid[2], initialGrid[3], initialGrid[0], initialGrid[1]
    else:
        # Performs a vertical flip on the grid
        initialGrid[0], initialGrid[1], initialGrid[2], initialGrid[3] = initialGrid[1], initialGrid[0], initialGrid[3], initialGrid[2]

# Prints the final orientation for the grid
print(initialGrid[0], initialGrid[1])
print(initialGrid[2], initialGrid[3])
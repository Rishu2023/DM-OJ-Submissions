#-----------------------------------------------------------------------------
# Name:  CCC '21 S2 - Modern Art (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------

# Gets the dimensions of the canvas and the number of strokes
numRowsCanvas = int(input())
numColsCanvas = int(input())
numStrokes = int(input())

# Initializes lists to keep track of the strokes of the rows and columns
rowStrokeCounts = [0] * numRowsCanvas
colStrokeCounts = [0] * numColsCanvas

# Get strokes from the artist
for _ in range(numStrokes):
    strokeInput = input().split()
    strokeDirection = strokeInput[0]
    strokeIndex = int(strokeInput[1]) - 1
    
    # Updates the appropriate row or column based on the stroke direction
    if strokeDirection == 'R':
        rowStrokeCounts[strokeIndex] += 1
    else:
        colStrokeCounts[strokeIndex] += 1

# Counts the number of cells that are gold after all strokes
numGoldCells = 0
for rowIndex in range(numRowsCanvas):
    for colIndex in range(numColsCanvas):
        if (rowStrokeCounts[rowIndex] + colStrokeCounts[colIndex]) % 2 == 1:
            numGoldCells += 1

# Prints at last the total count of gold cells
print(numGoldCells)
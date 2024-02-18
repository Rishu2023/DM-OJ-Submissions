#-----------------------------------------------------------------------------
# Name:  CCC '00 S4 - Golf (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------
teeToHoleDistance = int(input())
numClubs = int(input())

clubDistances = []
for _ in range(numClubs):
    clubDistance = int(input())
    clubDistances.append(clubDistance)

# Dynamic programming approach to find the minimum number of strokes
minStrokesRequired = [float('inf') for _ in range(teeToHoleDistance + 1)]
minStrokesRequired[0] = 0

for i in range(1, teeToHoleDistance + 1):
    for clubDistance in clubDistances:
        if i - clubDistance >= 0:
            if 1 + minStrokesRequired[i - clubDistance] < minStrokesRequired[i]:
                minStrokesRequired[i] = 1 + minStrokesRequired[i - clubDistance]

if minStrokesRequired[-1] != float('inf'):
    print(f"Roberta wins in {minStrokesRequired[-1]} strokes.")
else:
    print("Roberta acknowledges defeat.")
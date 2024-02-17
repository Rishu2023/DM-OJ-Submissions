#-----------------------------------------------------------------------------
# Name: ECOO '15 R1 P1 - When You Eat Your Smarties (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

smartieColor = ""
smartieColorCounts = [0] * 8
totalTime = 0
smartieBoxCount = 0

try:
  while smartieBoxCount < 10:
    smartieColor = input()
    if smartieColor == "end of box":
       for count in range(7):
         if smartieColorCounts[count] % 7 == 0:
           totalTime += (smartieColorCounts[count] // 7) * 13
         else:
           totalTime += 13 * ((smartieColorCounts[count] // 7) + 1)
       print(int(totalTime))
       smartieColorCounts = [0] * 8
       totalTime = 0
    elif smartieColor == "orange":
      smartieColorCounts[0] += 1
    elif smartieColor == "blue":
      smartieColorCounts[1] += 1
    elif smartieColor == "green":
      smartieColorCounts[2] += 1
    elif smartieColor == "yellow":
      smartieColorCounts[3] += 1
    elif smartieColor == "pink":
      smartieColorCounts[4] += 1
    elif smartieColor == "violet":
      smartieColorCounts[5] += 1
    elif smartieColor == "brown":
      smartieColorCounts[6] += 1
    elif smartieColor == "red":
      totalTime += 16
except EOFError:
  pass
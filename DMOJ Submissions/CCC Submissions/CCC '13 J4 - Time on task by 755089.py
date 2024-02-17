#-----------------------------------------------------------------------------
# Name: CCC '13 J4 - Time on task (main.py)
# Author:      Aryan Mittal
# Created:     15-Feb-2024
# Updated:     15-Feb-2024
#---------------------------------------------------------------------------

totalTimeChores = int(input())
choresYouChooseFrom = int(input())
theThings = []
sum = 0
max = 0

for count in range(choresYouChooseFrom):
    theChore = int(input())
    theThings.append(theChore)

theThings.sort()

for count in range(len(theThings)):
    if sum > totalTimeChores:
        break
    else:
        sum += theThings[count]
        max += 1

print(max-1)
#-----------------------------------------------------------------------------
# Name:  CCC '16 S2 - Tandem Bicycle (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------
# Get the type of question and input data
questionType = int(input())  # 1 is for the minimum total speed, 2 is for the maximum total speed
numCitizens = int(input())  # Number of citizens participating
dmojistanSpeedsInput = input()  # Speed of citizens of Dmojistan separated by spaces
peglandSpeedsInput = input()  # Speed of citizens of Pegland separated by spaces

# Converts input strings to lists of integers
dmojistanSpeeds = list(map(int, dmojistanSpeedsInput.split()))
peglandSpeeds = list(map(int, peglandSpeedsInput.split()))

# Initializes total speed to calculate total speed
totalSpeed = 0

# Sorts lists in descending order for question 1 and in ascending order for question 2
if questionType == 1:
    dmojistanSpeeds.sort(reverse=True)
    peglandSpeeds.sort(reverse=True)
else:
    dmojistanSpeeds.sort(reverse=True)
    peglandSpeeds.sort()

# Calculates the total speed based on question type
for i in range(len(dmojistanSpeeds)):
    if dmojistanSpeeds[i] >= peglandSpeeds[i]:
        totalSpeed += dmojistanSpeeds[i]
    else:
        totalSpeed += peglandSpeeds[i]

# Prints the total speed
print(totalSpeed)
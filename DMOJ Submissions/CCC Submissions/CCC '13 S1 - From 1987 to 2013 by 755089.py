#-----------------------------------------------------------------------------
# Name: CCC '13 S1 - From 1987 to 2013 (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     15-Feb-2024
# Updated:     15-Feb-2024
#---------------------------------------------------------------------------
def hasDistinctDigits(inputYear):
    strYear = str(inputYear)
    uniqueDigits = set(strYear)
    return len(uniqueDigits) == len(strYear)

def findNextYearWithDistinctDigits(startingYear):
    nextYear = startingYear + 1
    while not hasDistinctDigits(nextYear):
        nextYear += 1
    return nextYear

inputYear = int(input())

nextYearWithDistinctDigits = findNextYearWithDistinctDigits(inputYear)

print(nextYearWithDistinctDigits)

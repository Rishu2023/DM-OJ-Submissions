#-----------------------------------------------------------------------------
# Name:  A Plus B by 755089 (main.py)
# Author:      Aryan Mittal
# Created:     15-Feb-2024
# Updated:     15-Feb-2024
#---------------------------------------------------------------------------

theNumber = int(input())

for i in range(theNumber):
    letterA, letterB = map(int, input().split())
    print(letterA + letterB)
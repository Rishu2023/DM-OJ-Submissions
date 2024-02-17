#-----------------------------------------------------------------------------
# Name:  CCC '07 J1 - Who is in the Middle? (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------
# Lets the user input the weights of the three bowls
firstWeight = int(input())
secondWeight = int(input())
thirdWeight = int(input())

# Determines and outputs the weight of Mama Bear's bowl
mamaBearWeight = max(min(firstWeight, secondWeight), min(max(firstWeight, secondWeight), thirdWeight))
print(mamaBearWeight)
#-----------------------------------------------------------------------------
# Name:        CCC '19 J1 - Winning Score (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

#Asks for the input for the different type of goals by different teams
applesOne = int(input())
applesTwo = int(input())
applesThree = int(input())

bananasOne = int(input())
bananasTwo = int(input())
bananasThree = int(input())

#Manipulates variables through multiplication of each of the inputs and utilizes if statements to figure out correct output for which team has won
applesTotalScore = (applesOne * 3) + (applesTwo * 2) + (applesThree * 1)

bananasTotalScore = (bananasOne * 3) + (bananasTwo * 2) + (bananasThree * 1)

if applesTotalScore > bananasTotalScore:
  print("A")
elif bananasTotalScore > applesTotalScore:
  print("B")
else:
  print("T")
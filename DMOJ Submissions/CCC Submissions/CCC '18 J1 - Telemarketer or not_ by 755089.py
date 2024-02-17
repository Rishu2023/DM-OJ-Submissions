#-----------------------------------------------------------------------------
# Name:        CCC '18 J1 - Telemarkter or not? (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

#User inputs the last four digits of the telephone number
firstNumber = int(input())
secondNumber = int(input())
thirdNumber = int(input())
fourthNumber = int(input())

#Checks if the number matches the pattern for a telemarketer number and prints statements based on conditions
if (firstNumber == 8 or firstNumber == 9) and (fourthNumber == 8 or fourthNumber == 9) and (secondNumber == thirdNumber):
  print("ignore")
else:
  print("answer")
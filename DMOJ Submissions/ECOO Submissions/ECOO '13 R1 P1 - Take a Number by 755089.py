#-----------------------------------------------------------------------------
# Name: ECOO '13 R1 P1 - Take a Number (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

nextNumberInMachine = 0
studentsWaiting = 0
studentsLate = 0
nextNumberInMachine = int(input())
inputCommand = ""

while inputCommand != "EOF":
  inputCommand = input()
  if inputCommand == "TAKE":
    nextNumberInMachine += 1
    studentsWaiting += 1
    studentsLate += 1
  elif inputCommand == "SERVE":
    studentsWaiting -= 1
  elif inputCommand == "CLOSE":
    print(studentsLate, studentsWaiting, nextNumberInMachine)
    studentsLate = 0
    studentsWaiting = 0
  if nextNumberInMachine == 1000:
    nextNumberInMachine = 1
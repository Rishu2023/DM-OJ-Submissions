#-----------------------------------------------------------------------------
# Name: CCC '19 J3 - Cold Compress (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

numberOfStrings = int(input())
theStrings = []

for i in range(numberOfStrings):
  line = input()
  theStrings.append(line)

for j in range (numberOfStrings):
  theCounter = 0
  theMessage = " "
  variableK = theStrings[j]
  for i in range(len(variableK)):
    if i!=len(variableK)-1 and variableK[i]==variableK[i + 1]:
      theCounter = theCounter+1
    else:
      theMessage = theMessage + " " + str(theCounter + 1) + " " + variableK[i]
      theEncodedMessage = theMessage[2:len(theMessage)]
      theCounter = 0
  print(theEncodedMessage)
#-----------------------------------------------------------------------------
# Name:  CCC '11 S2 - Multiple Choice (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------
#Allows user to input the responses in the first line and checks how many questions were answered correctly 
theLines = int(input())
theStudent = []
theCounter = 0

for i in range(theLines):
  theStudent.append(input())
for i in range(theLines):
  theTemp = input()
  if theTemp == theStudent[i]:
     theCounter += 1
print(theCounter)
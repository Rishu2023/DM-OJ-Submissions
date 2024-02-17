#-----------------------------------------------------------------------------
# Name:  COCI '06 Contest 5 #1 Trik (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

theActions = input()
thePosition = [1, 0, 0]

for i in range(len(theActions)):
  if theActions[i] == "A":
    og = thePosition[0]
    thePosition[0] = thePosition[1]
    thePosition[1] = og
  elif theActions[i] == "B":
    og = thePosition[1]
    thePosition[1] = thePosition[2] 
    thePosition[2] = og
  else:
    og = thePosition[2]
    thePosition[2] = thePosition[0]
    thePosition[0] = og

if thePosition[0] == 1:
    print(1)
elif thePosition[1] == 1:
    print(2)
else:
    print(3)
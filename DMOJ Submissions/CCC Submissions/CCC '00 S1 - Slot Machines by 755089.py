#-----------------------------------------------------------------------------
# Name:  CCC '00 S1 - Slot Machines (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

theQuarters = int(input())
machineOnePlays = int(input())
machineTwoPlays = int(input())
machineThreePlays = int(input())

totalPlays = 0

while theQuarters > 0:
  theQuarters -= 1
  totalPlays += 1
  machineOnePlays += 1
  if machineOnePlays == 35:
    theQuarters += 30
    machineOnePlays = 0
  if theQuarters > 0:
    theQuarters -= 1
    totalPlays += 1
    machineTwoPlays += 1
    if machineTwoPlays == 100:
        theQuarters += 60
        machineTwoPlays = 0

    if theQuarters > 0:
      theQuarters -= 1
      totalPlays += 1
      machineThreePlays += 1
      
    if machineThreePlays == 10:
        theQuarters += 9
        machineThreePlays = 0
print("Martha plays " + str(totalPlays) + " times before going broke." )

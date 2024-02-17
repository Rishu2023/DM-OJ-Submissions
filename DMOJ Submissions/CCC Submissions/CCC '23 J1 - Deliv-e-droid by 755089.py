#-----------------------------------------------------------------------------
# Name: CCC '23 J1 - Deliv-e-droid (main.py)
# Author:      Aryan Mittal
# Created:     15-Feb-2024
# Updated:     15-Feb-2024
#---------------------------------------------------------------------------

thePackages = int(input())
theCollisions = int(input())

totalPoints = (thePackages * 50) - (theCollisions * 10)

if thePackages > theCollisions:
    totalPoints += 500

print(totalPoints)
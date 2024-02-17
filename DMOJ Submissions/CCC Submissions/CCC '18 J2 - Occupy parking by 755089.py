#-----------------------------------------------------------------------------
# Name:  CCC '18 J2 - Occupy parking (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------
theSpots = int(input())
yesterdaySpots = input()
todaySpots = input()

counterOfSpots = 0

for i in range (0, theSpots):
  if (yesterdaySpots[i] == 'C' and todaySpots[i] =='C'):
      counterOfSpots += 1
print(counterOfSpots)
#-----------------------------------------------------------------------------
# Name: CCC '20 J2 - Epidemiology (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

theTotalPeople = int(input())
intialInfected = int(input())
theInfectionRate = int(input())
dayCounter = 0
theCurrentlyInfected = intialInfected

while theCurrentlyInfected <= theTotalPeople:
  theCurrentlyInfected += intialInfected * theInfectionRate
  intialInfected *= theInfectionRate
  dayCounter += 1

print(dayCounter)
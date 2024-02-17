#-----------------------------------------------------------------------------
# Name:        CCC '15 J1 - Special Day (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

# Allows the user to input the month and the day
theMonth = int(input())
theDay = int(input())

#Utilizes the inputs to check if the date matches with February 18
if theMonth < 2:
  print("Before")
elif theMonth > 2:
  print("After")
elif theMonth == 2:
  if theDay == 18:
    print("Special")
  elif theDay < 18:
    print("Before")
  elif theDay > 18:
    print("After")
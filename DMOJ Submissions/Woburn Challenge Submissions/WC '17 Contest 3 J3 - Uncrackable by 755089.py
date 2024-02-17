#-----------------------------------------------------------------------------
# Name:  WC '17 Contest 3 J3 - Uncrackable (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

thePassword = input()
theUppercase = 0
theLowercase = 0
theDigits = 0

if 8 <= len(thePassword) <= 12:
  for i in range(len(thePassword)):
    if thePassword[i].isupper():
      theUppercase += 1
    elif thePassword[i].islower():
      theLowercase += 1
    elif thePassword[i].isdigit():
      theDigits += 1

if (theUppercase >= 2) and (theLowercase >= 3) and (theDigits >= 1):
  print("Valid")
else:
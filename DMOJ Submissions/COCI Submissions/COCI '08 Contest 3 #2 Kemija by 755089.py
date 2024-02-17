#-----------------------------------------------------------------------------
# Name:  COCI '08 Contest 3 #2 Kemija (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

theEncodedSentence = input().strip()

theDecodedSentence = ""
theVowels = {"a","e","i","o","u"}
theCounter = 0

while theCounter < len(theEncodedSentence):
  if theEncodedSentence[theCounter] in theVowels:
    theDecodedSentence += theEncodedSentence[theCounter]
    theCounter += 3
  else:
    theDecodedSentence += theEncodedSentence[theCounter]
    theCounter += 1

print(theDecodedSentence)
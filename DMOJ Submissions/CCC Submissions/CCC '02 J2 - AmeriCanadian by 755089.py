#-----------------------------------------------------------------------------
# Name: CCC '02 J2 - AmeriCanadian (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

theWord = input().strip()
fullListOfWords = []

while theWord != "quit!":
  if (len(theWord) > 4) and (theWord[-2:] == "or") and theWord[-3] not in "aeiouy":
    theWord = theWord[:-2] + "our"
  fullListOfWords.append(theWord)
  theWord = input().strip()
print("\n".join(fullListOfWords))
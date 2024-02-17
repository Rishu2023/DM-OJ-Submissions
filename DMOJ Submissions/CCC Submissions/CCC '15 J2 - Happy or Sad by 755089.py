#-----------------------------------------------------------------------------
# Name:        CCC '15 J2 - Happy or Sad (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

# Reads and takes in the input text message from the user
userMessage = input()

# Counts the occurences of happy and sad emoticons and determines overall mode based on the counts
happyEmoticonCount = userMessage.count(":-)")
sadEmoticonCount = userMessage.count(":-(")
if (happyEmoticonCount == 0) and (sadEmoticonCount == 0):
  print("none")
elif happyEmoticonCount == sadEmoticonCount:
  print("unsure")
elif happyEmoticonCount > sadEmoticonCount:
  print("happy")
else:
  print("sad")
#-----------------------------------------------------------------------------
# Name:  CCC '11 S1 - English or French? (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------
# Reads the number of lines of text
numLines = int(input())

# Concatenates all the lines of text into a single string
text = ""
for i in range(numLines):
    text += input().lower()

# Initializes counters to check the occurrences of 's' and 't'
countS = 0
countT = 0

# Counts the occurrences of 's' and 't' in the text
for letter in text:
    if letter == "s":
        countS += 1
    elif letter == "t":
        countT += 1

# Compares the counts of 's' and 't' to determine which language it is
if countT > countS:
    print("English")
else:
    print("French")
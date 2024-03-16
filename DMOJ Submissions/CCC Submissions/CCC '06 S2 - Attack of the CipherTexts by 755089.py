#-----------------------------------------------------------------------------
# Name:  CCC '06 S2 - Attack of the CipherTexts (main.py)
# Author:      Aryan Mittal
# Created:     22-Feb-2024
# Updated:     22-Feb-2024
#---------------------------------------------------------------------------
thePlainText = input()
theCorresponding = input()
theDecoding = input()

fullCode = {
}

fullKeySet = []
fullValSet = []

for count in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
    fullKeySet.append(count)
    fullValSet.append(count)

for count in range(len(thePlainText)):
    fullCode[theCorresponding[count]] = thePlainText[count]
    if theCorresponding[count] in fullKeySet: fullKeySet.remove(theCorresponding[count])
    if thePlainText[count] in fullValSet: fullValSet.remove(thePlainText[count])

if (len(fullKeySet) == 1):
    fullCode[fullKeySet[0]] = fullValSet[0]

fullOutput = ""

for count in range(len(theDecoding)):
    if theDecoding[count] in fullCode.keys():
        fullOutput += fullCode[theDecoding[count]]
    else:
        fullOutput += "."

print(fullOutput)
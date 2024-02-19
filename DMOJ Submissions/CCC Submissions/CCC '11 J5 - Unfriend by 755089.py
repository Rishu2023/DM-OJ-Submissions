#-----------------------------------------------------------------------------
# Name:  CCC '11 J5 - Unfriend (main.py)
# Author:      Aryan Mittal
# Created:     18-Feb-2024
# Updated:     18-Feb-2024
#---------------------------------------------------------------------------
numPeople = int(input())

# Creates an adjacency list to store the relationships between people
invitationGraph = [[] for _ in range(numPeople + 1)]
for i in range(numPeople - 1):
    inviter = int(input())
    invitationGraph[inviter].append(i + 1)

# Initializes a set to store subsets and a list to store all subsets
currentSubset = set()
allSubsets = []

def generateAllSubsets(startIndex):
    if startIndex == numPeople:
        allSubsets.append(currentSubset.copy())
    else:
        currentSubset.add(startIndex)
        generateAllSubsets(startIndex + 1)
        currentSubset.remove(startIndex)
        generateAllSubsets(startIndex + 1)

generateAllSubsets(1)

count = 0
# Iterates over all the subsets and check if they can be removed
for currentSubset in allSubsets:
    for friend in range(1, numPeople):
        # Only counts subsets that include the parent node (friend to be removed)
        # and all its children (invitees of that friend)
        if (friend in currentSubset and
                not all(invitee in currentSubset for invitee in invitationGraph[friend])):
            break
    else:
        count += 1

print(count)
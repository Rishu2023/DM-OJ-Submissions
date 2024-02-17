#-----------------------------------------------------------------------------
# Name:  CCC '08 J2 - Do the Shuffle (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

thePlaylist = ["A", "B", "C", "D", "E"]

while True:
  theButton = int(input())
  theTimes = int(input())
  if theButton == 1:
    for i in range(theTimes):
      thePlaylist.append(thePlaylist[0])
      thePlaylist.pop(0)
  elif theButton == 2:
    for i in range(theTimes):
      thePlaylist.insert(0, thePlaylist[-1])
      thePlaylist.pop(-1)
  elif theButton == 3:
    for i in range(theTimes):
      thePlaylist[0], thePlaylist[1] = thePlaylist[1], thePlaylist[0]
  else:
    break
for song in thePlaylist:
  print(song, end=" ")
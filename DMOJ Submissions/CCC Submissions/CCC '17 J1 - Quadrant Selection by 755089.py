#-----------------------------------------------------------------------------
# Name:  CCC '17 J1 - Quadrant Selection (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------

xCoordinate = int(input())
yCoordinate = int(input())
if (xCoordinate > 0) and (yCoordinate > 0):
    print("1")
if (xCoordinate < 0) and (yCoordinate > 0):
    print("2")
if (xCoordinate < 0) and (yCoordinate < 0):
    print("3")
if (xCoordinate > 0) and (yCoordinate < 0):
    print("4")
#-----------------------------------------------------------------------------
# Name:  CCC '16 J4 - Arrival Time (main.py)
# Author:      Aryan Mittal
# Created:     18-Feb-2024
# Updated:     18-Feb-2024
#---------------------------------------------------------------------------
departureTime = input()
departureHour, departureMinute = departureTime.split(":")
departureHour = int(departureHour)
departureMinute = int(departureMinute)

commuteDuration = 2 * 60

while commuteDuration != 0:
    if 7 <= departureHour < 10 or 15 <= departureHour < 19:
        departureMinute += 10
        commuteDuration -= 5
    else:
        departureMinute += 10
        commuteDuration -= 10

    if departureMinute == 60:
        departureHour += 1
        departureMinute = 0
    if departureHour == 24:
        departureHour = 0

if departureHour < 10:
    departureHour = "0" + str(departureHour)
if departureMinute == 0:
    departureMinute = "00"
print(str(departureHour) + ":" + str(departureMinute))
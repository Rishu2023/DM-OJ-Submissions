#-----------------------------------------------------------------------------
# Name:  CCC '06 J1 - Canadian Calorie Counting (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

# A small mapping that matches each food to its calorie count
theMenu = {
  "theBurgers": {1: 461, 2: 431, 3: 420, 4: 0},
  "theDrinks": {1: 130, 2: 160, 3: 118, 4: 0},
  "theSides": {1: 100, 2: 57, 3: 70, 4: 0},
  "theDesserts": {1: 167, 2: 266, 3: 75, 4: 0}
}

# Input allows to read customer's choice for food
burgerChoice = int(input())
sideChoice = int(input())
drinkChoice = int(input())
dessertChoice = int(input())

# This calculates total calorie count and outputs it
totalCalories = theMenu["theBurgers"][burgerChoice] + theMenu["theDrinks"][drinkChoice] + theMenu["theSides"][sideChoice] + theMenu["theDesserts"][dessertChoice]
print("Your total Calorie count is {}.".format(totalCalories))
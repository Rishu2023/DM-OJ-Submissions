#-----------------------------------------------------------------------------
# Name:  DMOPC '16 Contest 1 P0 - C.C. and Cheese-kun (main.py)
# Purpose:    If statements
#
# Author:      Aryan Mittal
# Created:     09-Feb-2024
# Updated:     09-Feb-2024
#---------------------------------------------------------------------------

# Obtains user's input for the width and extra cheese
pizzaWidth = int(input())
pizzaExtraCheesiness = int(input())

# Checks the satisfaction level for C.C for her pizza
if (pizzaWidth == 3) and (pizzaExtraCheesiness >= 95):
  print("C.C. is absolutely satisfied with her pizza.")
elif (pizzaWidth == 1) and (pizzaExtraCheesiness <= 50):        
  print("C.C. is fairly satisfied with her pizza.")
else:
  print("C.C. is very satisfied with her pizza.")
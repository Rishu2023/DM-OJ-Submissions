S = int(input())
M = int(input())
L = int(input())

numOfTreats = (S * 1) + (M * 2) + (L * 3)
if numOfTreats >= 10:
  print("happy")
else:
  print("sad")
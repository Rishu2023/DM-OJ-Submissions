G1 = input()
G2 = input()
G3 = input()
G4 = input()
G5 = input()
G6 = input()

wCount = G1.count('W') + G2.count('W') + G3.count('W') + G4.count('W') + G5.count('W') + G6.count('W')

if wCount >= 5:
  print(1)
elif wCount >= 3 and wCount < 5:
  print(2)
elif wCount >= 1 and wCount < 3:
  print(3)
else:
  print(-1)
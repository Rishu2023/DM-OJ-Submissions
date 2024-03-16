V = int(input())
VC = input()
VA = 0
VB = 0 

for votes in VC:
  if votes == "A":
    VA += 1;
  else:
    VB += 1;

if VA > VB:
  print("A")
elif VB > VA:
  print("B")
else:
  print("Tie")

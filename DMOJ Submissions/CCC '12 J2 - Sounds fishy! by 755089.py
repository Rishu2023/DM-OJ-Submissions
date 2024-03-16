A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A < B < C < D:
  print("Fish Rising")
elif D < C < B < A:
  print("Fish Diving")
elif D == C == B == A:
  print("Fish At Constant Depth")
else:
  print("No Fish")

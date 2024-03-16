n = int(input())
A = 100
D = 100

for count in range(n):
  rollA, rollD = map(int, input().split())
  if rollA > rollD:
    D -= rollA
  elif rollD > rollA:
    A -= rollD
  
print(A)
print(D)
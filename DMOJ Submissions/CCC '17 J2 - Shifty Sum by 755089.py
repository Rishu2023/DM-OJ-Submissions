N = int(input())
k = int(input())

sum = N

for count in range(1,k+1):
  sum += N * (10**count)
  
print(sum)

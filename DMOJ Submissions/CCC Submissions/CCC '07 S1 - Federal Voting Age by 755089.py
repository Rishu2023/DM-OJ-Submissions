n = int(input())
results = []
for count in range(n):
  birthday = input()
  y, m, d = map(int, birthday.split())
  y = int(y)
  m = int(m)
  d = int(d)
  if y < 1989:
    results.append("Yes")
  elif (y == 1989) and (m < 2):
    results.append("Yes")
  elif (y == 1989) and (m == 2) and (d <= 27):
    results.append("Yes")
  else:
    results.append("No")

for i in results:
  print(i)

B = int(input())

kPa = (5 * B) - 400
print(kPa)

if kPa < 100:
  print(1)
elif kPa == 100:
  print(0)
else:
  print(-1)

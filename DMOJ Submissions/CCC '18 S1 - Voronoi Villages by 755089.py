numVillages = int(input())
villages = list()
for count in range(numVillages):
  villages.append(float(input()))

distances = list()

villages.sort()

for count in range(1, numVillages - 1):
  distances.append((villages[count + 1] - villages[count]) / 2 + (villages[count] - villages[count - 1]) / 2)

distances.sort()
print(distances[0])
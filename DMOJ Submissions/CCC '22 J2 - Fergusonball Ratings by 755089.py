N = int(input())
totalStars = 0
for count in range(N):
  numOfPoints = int(input())
  numOfFouls = int(input())
  starRating = (5 * numOfPoints) - (3 * numOfFouls)
  if starRating > 40:
    totalStars += 1
if totalStars == N:
  print(str(totalStars) + "+") 
else:
  print(totalStars)
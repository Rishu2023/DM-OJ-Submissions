angleOne = int(input())
angleTwo = int(input())
angleThree = int(input())

if angleOne + angleTwo + angleThree != 180:
  print("Error")
elif (angleOne == 60) and (angleTwo == 60) and (angleThree == 60):
  print("Equilateral")
elif (angleOne == angleTwo) or (angleOne == angleThree) or (angleTwo == angleThree):
  print("Isosceles")
else:
  print("Scalene")
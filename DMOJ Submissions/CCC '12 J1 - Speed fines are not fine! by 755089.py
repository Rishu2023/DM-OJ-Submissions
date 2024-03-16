speedLimit = int(input())
speedOfCar = int(input())

if speedLimit >= speedOfCar:
  print("Congratulations, you are within the speed limit!")
elif 1 <= (speedOfCar - speedLimit) <= 20:
  print("You are speeding and your fine is $100.")
elif 21 <= (speedOfCar - speedLimit) <= 30:
  print("You are speeding and your fine is $270.")
else:
  print("You are speeding and your fine is $500.")

n = int(input())

totalSpiciness = 0

peppers = {
"Poblano": 1500,
"Mirasol": 6000,
"Serrano": 15500,
"Cayenne": 40000,
"Thai": 75000,
"Habanero": 125000
}

for count in range(n):
  totalSpiciness += peppers[input()]

print(totalSpiciness)

numOfAntennaes = int(input())
numOfEyes = int(input())

if (numOfAntennaes >= 3) and (numOfEyes <= 4):
  print("TroyMartian")

if (numOfAntennaes <= 6) and (numOfEyes >= 2):
  print("VladSaturnian")

if (numOfAntennaes <= 2) and (numOfEyes <= 3):
  print("GraemeMercurian")

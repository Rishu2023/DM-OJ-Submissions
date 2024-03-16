LetterList = ['I','O','S','H','Z','X','N']
Word = input()

valid = True
for letter in Word:
    if letter not in LetterList:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")

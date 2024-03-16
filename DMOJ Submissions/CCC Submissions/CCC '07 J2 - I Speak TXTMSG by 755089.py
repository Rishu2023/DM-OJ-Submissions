TranslationTable = {
  'CU': 'see you', 
  ':-)': "I'm happy", 
  ':-(': "I'm unhappy", 
  ';-)': 'wink', 
  ':-P': 'stick out my tongue',
  '(~.~)': 'sleepy', 
  'TA': 'totally awesome',
  'CCC': 'Canadian Computing Competition',
  'CUZ': 'because',
  'TY': 'thank-you',
  'YW': "you're welcome", 
  'TTYL': 'talk to you later'
}

while True:
  UserInput = input()
  if UserInput == 'TTYL':
      print('talk to you later')
      break
  elif UserInput in TranslationTable:
      print(TranslationTable[UserInput])
  else:
      print(UserInput)

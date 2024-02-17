#-----------------------------------------------------------------------------
# Name: COCI '08 Contest 1 #2 Ptice (main.py)
# Purpose: Loop Challenges
# Author:      Aryan Mittal
# Created:     13-Feb-2024
# Updated:     13-Feb-2024
#---------------------------------------------------------------------------

numberOfQuestions = int(input())
theCorrectAnswers = input().strip()
adrianSequence = "ABC" * ((numberOfQuestions // 3) + 1)
brunoSequence = "BABC" * ((numberOfQuestions // 4) + 1)
goranSequence = "CCAABB" * ((numberOfQuestions // 6) + 1)
adrianScore = sum(1 for a, b in zip(theCorrectAnswers, adrianSequence) if a == b)
brunoScore = sum(1 for a, b in zip(theCorrectAnswers, brunoSequence) if a == b)
goranScore = sum(1 for a, b in zip(theCorrectAnswers, goranSequence) if a == b)
theMaximumScore = max(adrianScore, brunoScore, goranScore)

print(theMaximumScore)
if adrianScore == theMaximumScore:
  print("Adrian")
if brunoScore == theMaximumScore:
  print("Bruno")
if goranScore == theMaximumScore:
  print("Goran")
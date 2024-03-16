N = int(input())
scores = []
for count in range(N):
    score = int(input())
    scores.append(score)

uniqueScores = sorted(set(scores), reverse=True)
bronzeLevel = uniqueScores[2]
bronzeLevelThird = scores.count(bronzeLevel)
print(bronzeLevel, bronzeLevelThird)

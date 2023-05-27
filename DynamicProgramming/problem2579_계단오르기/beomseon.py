N = int(input())

scores = [0] * (N+1)
for i in range(1, N+1):
  scores[i] = int(input())

maxScore = [0] * (N+1)
if(N == 1):
  print(scores[1])

else:
  maxScore[1] = scores[1]
  maxScore[2] = scores[1] + scores[2]
  for i in range(3, N+1):
    maxScore[i] = max(maxScore[i-2]+scores[i], maxScore[i-3]+scores[i-1]+scores[i])

  print(maxScore[N])

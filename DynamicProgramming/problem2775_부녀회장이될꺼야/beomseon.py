T = int(input())

for i in range(T):
  k = int(input())
  n = int(input())

  people = [[0]*n for _ in range(k+1)]

  for j in range(n):
    people[0][j] = j+1
  
  for m in range(k):
    for j in range(n):  # j:몇번째 열의 값을 구할지
      result = 0
      for l in range(j+1):  # l: 0부터 j까지 
        result += people[m][l]  
      people[m+1][j] = result

  print(people[k][n-1])
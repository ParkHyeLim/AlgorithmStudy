def dfs(a, b):  
  if a == b:
    return
  visited[a-1] = 1
  for i in range(N):
    if (visited[i] == 0) and (graph[a-1][i] == 1):
      dfs(i+1, b)
        
            
N = int(input())  # 사람 수
a, b = map(int, input().split())  # 촌수를 계산해야하는 두 사람
graph = [[0]*N for i in range(N)] 
M = int(input())  #관계의 개수

for i in range(M):
  x, y = map(int, input().split())    #부모 자식간의 관계가 주어진 것들에 대해 표시
  graph[x-1][y-1] = 1
  graph[y-1][x-1] = 1

visited = [0]*N   #방문 확인 위해

dfs(a, b)
if(visited[b-1] == 0):
  print(-1)
else:
  print(sum(visited)-1)
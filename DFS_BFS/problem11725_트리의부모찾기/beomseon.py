import sys
sys.setrecursionlimit(10**6) # 백준 최대 재귀깊이1000 이므로 변경해줌
input = sys.stdin.readline  # input 속도빠르게

def dfs(num):
  visited[num-1] = 1  #방문 표시
  for i in graph[num]:  
    if(visited[i-1] == 0):
      parent[i-1] = num
      dfs(i)

N = int(input())  # 노드 수
graph = [[] for i in range(N+1)] # 인접 행렬 사용시 메모리초과됨 -> 인접리스트사용 (리스트0부터 시작하므로 수 맞춰주기 위해 +1)

for i in range(N-1):  # 노드간의 연결관계 표현
  x, y =map(int, input().split())
  graph[x].append(y) 
  graph[y].append(x)

visited = [0]*N
parent = [0]*N  # 부모노드 저장

dfs(1)

for i in range(N-1):
  print(parent[i+1])

#         1
#      4	   6
#    2  7       3
#                  5
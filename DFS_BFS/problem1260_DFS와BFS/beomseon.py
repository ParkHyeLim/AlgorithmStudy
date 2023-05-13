from collections import deque

def dfs(V):
  visited[V-1] = 1  # ex) 1번정점 방문시 visited의 0번째 항목이 1로 변경 
  print(V, end=" ")
  for i in range(N):
    if (graph[V-1][i] == 1) and (visited[i] == 0):  #V번과 연결된 정점이 방문하지 않은 정점일경우 그 정점방문( dfs)
       dfs(i+1)

def bfs(V):
   q = deque()  
   q.append(V)  #처음 방문 정점 deque에 삽입
   visited2[V-1] = 1
   while q: # deque에 삽입된 정점들 pop해서 연결된 것 모두 확인되면 종료
    V = q.popleft() 
    print(V, end=" ")
    for i in range(N):
        if (graph[V-1][i] == 1) and (visited2[i] == 0):
          visited2[i] = 1 # 정점과 연결된 다른 정점들 방문 표시
          q.append(i+1)  # 정점과 연결된 다른 정점 deque에 삽입(이것들과 연결된 다음 정점 방문 때 pop해서 확인) 

N, M, V = map(int,input().split())

graph = [[0]*(N) for i in range (N)]  # 정점 개수에 따라 graph 배열 생성

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1   # 간선이 연결되어 있는 것을 1로 표시
    graph[b-1][a-1] = 1

visited = [0]*N #방문한 정점 확인위해 (방문하면 1로변경)
visited2 = [0]*N # 초기화 후 bfs로 확인하기 위해

dfs(V)
print()
bfs(V)


#인접행렬(각 정점의 연결관계표현) 이용 간선이 있을 때 1 없을 때 0으로
# 1 -> [0, 1, 1, 1]   (2 3 4와 간선 연결되어있음)
# 2 -> [1, 0, 0, 1]   (1 4 와 간선 연결)
# 3 -> [1, 0, 0, 1]   (1 4 와 간선 연결)
# 4 -> [1, 1, 1, 0]   (1 2 3 간선 연결)   => 대칭형태를 이룸
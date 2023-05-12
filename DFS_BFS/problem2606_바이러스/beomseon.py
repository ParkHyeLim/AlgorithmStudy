def dfs(V):
    visited[V-1] = 1    # 방문
    for i in range(N):    # 연결된 컴퓨터 확인
        if (visited[i] == 0) and (graph[V-1][i] == 1): # 방문하지 않았고 연결되어 있다면 방문 dfs 
            dfs(i+1)

N=int(input()) # 컴퓨터
M=int(input()) # 연결선

graph = [[0]*N for i in range(N)]    # 그래프

visited=[0]*(N) # 방문한 컴퓨터 표시

for i in range(M):      # 연결된 컴퓨터 표시
    a, b=map(int,input().split())
    graph[a-1][b-1] = 1 
    graph[b-1][a-1] = 1     # 양방향



dfs(1)  #1번컴퓨터부터
print(sum(visited)-1)   #1번컴퓨터와 연결된 컴퓨터의 수(1번 제외)
# 노드 수
N = int(input())

# 연결 수
node = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    x, y= map(int, input().split())
    node[x].append(y)
    node[y].append(x)

dep = 0
stack = [(1, dep)]
while stack:
    v, d = stack.pop()
    visited[v] = True
    for i in node[v]:
        if (visited[i] == False):
            parent[i] = v
            stack.append((i, dep+1))

for i in range(2, N+1):
    print(parent[i])

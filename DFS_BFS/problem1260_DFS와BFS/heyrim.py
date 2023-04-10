from collections import deque

N, M, V = map(int, input().split())
list1 = [[] for _ in range(N+1)]
count = 0

for i in range(M):
    num1, num2 = map(int, input().split())
    list1[num1].append(num2)
    list1[num2].append(num1)

for i in range(len(list1)):
    list1[i].sort()

def Dfs(List, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in List[v]:
        if (visited[i] == False):
            Dfs(List, i, visited)

visited = [False for _ in range(N+1)]
Dfs(list1, V, visited)

print()
def Bfs(List, v, visited):
    queue = deque([v]) # queue = [3]
    visited[v] = True
    while queue:
        v = queue.popleft() # v = 3 queue = []
        print(v, end=' ')
        for i in List[v]:
            if (visited[i] == False):
                visited[i] = True
                queue.append(i)  # queue = [i]
                  
visited = [False for _ in range(N+1)]
Bfs(list1, V, visited)

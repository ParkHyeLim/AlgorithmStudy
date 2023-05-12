# 컴퓨터 수
N = int(input())

# 연결 수
K = int(input())
compu = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(K):
    X, Y = map(int, input().split())
    compu[X].append(Y)
    compu[Y].append(X)

count = 0
stack = [1]
visited[1] = True
while stack:
    v = stack.pop()
    for i in compu[v]:
        if (not visited[i]):
            visited[i]= True
            stack.append(i)
            count += 1    

print(count)

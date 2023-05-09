visited = [[0]*1001]
DFS = []
BFS = []
bucket = [[0]*1001]*1001


def sol_DFS(tar):
    visited[tar] = 1
    DFS.push_back(tar)

    for i in range(len(bucket[tar])):
        if visited[bucket[tar][i]] == 0:  # 가지 않은 노드일 경우
            sol_DFS(bucket[tar][i])


def sol_BFS(tar):
    q = []
    visited[tar] = 1
    q.append(tar)

    while q.empty() == False:
        q.pop(0)
        BFS.push_back(tar)
        for i in range(len(bucket[tar])):
            if visited[bucket[tar][i]] == 0:
                q.append(bucket[tar][i])
                visited[bucket[tar][i]] = 1


def print_arr(v):
    for i in range(len(v)):
        print(v[i])


N, M, V = int(input())
for i in range(M):
    a, b = int(input())
    bucket[a].append(b)
    bucket[b].append(a)

for i in range(N):
    bucket[i].sort()

target = V
# DFS
sol_DFS(target)
print_arr(DFS)

# BFS
# DFS로 다녀간 visited 초기화
for i in range(N):
    visited[i] = 0

sol_BFS(target)
print_arr(BFS)

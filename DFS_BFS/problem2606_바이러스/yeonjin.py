MAX_NODE = 101
visited = [[0]*MAX_NODE]  # 해당 노드(i번째 인덱스)에 방문하였는지
DFS = []
bucket = [[]]*MAX_NODE  # i번째 bucket에는 i번 노드와 연결되어 있는 노드 번호가 있다.


def sol_DFS(target):
    if len(visited) > target:
        visited[target] = 1
        DFS.push_back(target)

        for i in len(bucket[target]):
            if visited[bucket[target][i]] == 0:  # 가지 않은 노드일 경우
                sol_DFS(bucket[target][i])


# N: 컴퓨터 수, M: 컴퓨터 쌍 수
N = int(input())
M = int(input())

for i in range(M):   # a와 b 컴퓨터가 서로 연결되어 있음
    a, b = map(int, input().split())
    bucket[a].append(b)
    bucket[b].append(a)

sol_DFS(1)
print(len(DFS)-1)  # 1번 컴퓨터를 통해 바이러스에 걸린 컴퓨터의 수

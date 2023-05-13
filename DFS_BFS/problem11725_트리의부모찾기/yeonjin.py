limit = 100, 000
n = int(input())  # 노드 개
level = [limit] * (n+1)   # 저장
parents = [0] * (n+1)   # 저장
q = []
level[1] = 1
parents[1] = -1

while n > 1:
    a, b = map(int, input().split())
    q.push([a, b])
    n -= 1

while q.length != 0:
    a = q[0][0]
    b = q[0][1]
    if level[a] == limit and level[b] == limit:
        q.push([a, b])
        q.remove(0)
    else:
        level[a]

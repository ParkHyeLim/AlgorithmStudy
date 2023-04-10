#2644

# 전체 사람의 수 : n
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두사람의 번호 : p, q
p, q = map(int, input().split())

# 부모 자신들간의 관계의 수 : m
m = int(input())

# 부모 자식간의 관계를 나타내는 두 번호 : x, y
family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

# 촌수
count = 0
stack = [(p, count)]
while stack:
    print(stack)
    v, c = stack.pop()
    visited[v] = True
    if (v == q):
        count = c
        break
    for i in family[v]:
        if (not visited[i]):
            stack.append((i,c+1))
            print(c)

           
if (count == 0):
    print(-1)
else:
     print(count)

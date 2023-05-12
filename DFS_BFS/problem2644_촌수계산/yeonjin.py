n = int(input())  # 사람 수
t1, t2 = map(int, input().split())  # 타겟 두 사람 번호
m = int(input())  # 관계 수
parents = [0] * (n+1)
boards = [[]] * (n+1)
answer = 0
found = False


def bsf(root, depth):
    if root == t1 or root == t2:
        if answer != 0:  # 두개 다 찾음
            found = True
            return
        answer += depth
    if len(boards) != 0:
        for b in boards[root]:
            bsf(b, depth+1)


while m:
    a, b = map(int, input().split())
    parents[b] = a
    boards[a].append(b)
    m -= 1

for i in range(1, n+1):
    if parents[i] == 0:     # 루트일 경우
        bsf(parents[i], 0)
        if answer != 0:
            break

if found:
    print(answer)
else:
    print(-1)

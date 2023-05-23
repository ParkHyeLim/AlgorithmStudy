N, M = map(int, input().split())
tmp = list(map(int, input().split()))
arr = sorted(tmp)

max_n = arr[len(arr)-1]
result = M
while max_n > M:
    rs = 0
    ri = len(arr) - 1
    while arr[ri] > max_n and ri >= 0:
        rs += (arr[ri] - max_n)
        ri -= 1

    if rs >= M:
        result = max_n
        break
    max_n -= 1

print(result)
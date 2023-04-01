# 블랙잭
n, m = map(int, input().split())
arr = input().split()
for e in range(len(arr)):
    arr[e] = int(arr[e])

answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = int(arr[i]+arr[j]+arr[k])
            if (answer < tmp) and (tmp <= m):
                answer = tmp

print(answer)

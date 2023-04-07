n, k = map(int, input().split())
arr = []
for i in range(n):
    tmp = int(input())
    if tmp <= k:
        arr.append(tmp)

ans = 0
for i in arr[::-1]:
    ans += k//i
    k -= (k//i)*i

print(ans)

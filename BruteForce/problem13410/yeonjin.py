# 거꾸로 구구단
n, k = map(int, input().split())
ans = 0
for i in range(k):
    num = int(str(i*k)[::-1])
    if ans < num:
        ans = num
print(ans)

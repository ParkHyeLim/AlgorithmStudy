n = int(input())
ans = 0
while True:
    if n % 5 == 0 or n <= 0:
        break
    n -= 3
    ans += 1
if n < 0:
    print(-1)
else:
    ans += n//5
    print(ans)
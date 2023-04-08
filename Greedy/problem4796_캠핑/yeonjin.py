num = 1
while True:
    l, p, k = map(int, input().split())
    if l == 0 and p == 0 and k == 0:
        break
    ans = (k//p)*l + (k % p if k % p <= l else l)
    s = "Case " + str(num) + ": " + str(ans)
    print(s)
    num += 1

T = int(input())
dp = [0 for i in range(10)]
dp[0] = 1
dp[1] = 2
dp[2] = 4

while T > 0:
    n = int(input())
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n-1])

    T -= 1

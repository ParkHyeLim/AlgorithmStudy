# 동전 총 N 종류
# 동전 값의 
# 동전 개수의 최솟값

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
num_coin = 0 # coin 개수

coins.sort()

for i in range(N-1, -1, -1):
    if (coins[i] <= K):
        num_coin += K//coins[i]
        K = K%coins[i]
    if (K == 0):
        break

print(num_coin)

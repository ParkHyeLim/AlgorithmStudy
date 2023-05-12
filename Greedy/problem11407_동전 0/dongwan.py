N, K = map(int, input().split()) #K는 금액 , N동전 종류

coins = [int(input()) for _ in range(N)] # 동전 종류만큼 반복

coins.sort(reverse=True)  # 동전의 가치가 큰 것부터 정렬해야 최소의 동전사용가능

count = 0 #현재까지 사용한 동전 개수

for coin in coins:
    if K == 0:  # K를 0으로 만들었으면 종료
        break
    count += K // coin  # 해당 동전으로 만들 수 있는 최대 개수를 더함
    K %= coin  # 남은 금액을 계산

print(count)

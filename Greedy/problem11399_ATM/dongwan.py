# 작은 값부터 채워서 최적해를 찾는 방향

# n : 줄 서 있는 사람
# p : 사람마다 돈을 인출하는데 걸리는 시간
n = int(input())
p = list(map(int, input().split()))

p_sorted = sorted(p) # 돈을 인출하는데 걸리는 시간이 적은 순으로 정렬

time = 0
result = 0

for i in range(n):
    time += p_sorted[i] # 돈을 인출하는 데 걸리는 시간을 누적
    result += time    # 누적된 시간을 결과에 더해줌

print(result)

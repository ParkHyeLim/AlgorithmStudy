# 방법 1 시간초과
# N = int(input())
# m = 1       # 자연수 1부터 전체탐색

# while True:
#     sum = 0          # 각 자리 수 합
#     for i in range( len(str(m)) ):
#         sum += int( str(m)[i] )

#     if (sum + m) == N:      # m의 분해합이 N인 경우
#         M = m         # m을 생성자 M이라 함
#         break
#     m += 1
# print(M)

# # ----------방법2--------- 역시 시간초과
def sum_func(m):
    sum = m
    while (m != 0):
        sum += m % 10
        m = m//10
    return sum


N = int(input())

M = 0
while (M < N):
    M += 1
    if sum_func(M) == N:
        break
print(M)

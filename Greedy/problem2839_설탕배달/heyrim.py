# 배달할 설탕 N 킬로그램
# 3 킬로, 5킬로 봉지
# 최대한 적은 봉지 출력 = 3의 배수와 5의 배수의 합을 만드는 최소

N = int(input())
min_reasult = float('inf')

for i in range(N//3+1):
    for j in range(N//5+1):
        if (i*3 + j*5 == N):
            min_reasult = min(min_reasult, i+j)

if (min_reasult == float('inf')):
    print(-1)
else:
    print(min_reasult)

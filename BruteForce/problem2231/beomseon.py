# N = int(input())
# a = []
# M = 0

# while(True):
#     M += 1
#     number = M
#     while(number != 0):       # 각 자리수의 합 구하기
#         a.append(number%10)
#         number = number//10
#     numberSum = M + sum(a)    # numberSum : 분해합
#     a=[]                      # a 초기화

#     if numberSum == N:
#         print(M)
#         break
#     else :
#         numberSum = 0
        
#     if N == M :
#         print(0)
#         break

N = int(input())

for i in range(1, N+1) :
    if i + sum(map(int, str(i))) == N :     # map을 이용하여 주어진 수의 각 자리수를 분리하여 int형으로 바꾸고 sum() 실행
        print(i)
        break
else:                                       # for - else문 이용 (for문이 break되지않고 모두 수행될 때만 else문 실행)
    print(0)    

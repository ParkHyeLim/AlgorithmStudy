N = int(input())
*A, = map(int, input().split())
B = list(map(int, input().split()))
S = 0

A.sort()
B.sort(reverse=True)

# 배열을 각각 오름차순, 내림차순으로 정렬하여 배열원소의 곱을 합친게 최소가 되도록
for i in range(N):
    S += A[i]*B[i]

print(S)
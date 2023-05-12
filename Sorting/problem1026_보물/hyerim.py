# 1026
# 길이 N / 정수형 배열 A, B
# S = A*B
# S를 최소로 하는 재배열 된 A

length = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
S = 0

# B의 가장 큰 값 * A의 가장 작은 값(B 재정렬x)
A_sorted = sorted(A)
print(A)
B_list = B.copy()
for i in range(length):
    B_max_index = B_list.index(max(B_list))
    A[B_max_index] = A_sorted[i]
    B_list[B_max_index] = -1

for i in range(length):
    S += A[i]*B[i]

print(S)

# B의 가장 큰 값 * A의 가장 작은 값(B 또한 재정렬 됨)
A.sort()
B.sort(reverse=True)

for i in range(length):
    S += A[i]*B[i]

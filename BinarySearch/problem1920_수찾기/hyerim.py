#1920 수 찾기

def binary_search(arr, target, arr_len):
    start = 0
    end = arr_len - 1

    while start <= end:
        mid = (start + end) // 2 # 중간점 찾기

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

N = int(input()) #A[N]
A = sorted(list(map(int, input().split()))) 

M = int(input()) #비교할 정수 개수
Numbers = list(map(int, input().split())) #비교할 정수

for num in Numbers:
    if binary_search(A, num, N):
        print(1)
    else:
        print(0)

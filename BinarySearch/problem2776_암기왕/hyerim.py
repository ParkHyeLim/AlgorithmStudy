#2776 암기왕 

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

for _ in range(int(input())): #테스트 케이스 개수
    N1 = int(input()) #수첩 1에 적어 놓은 정수 개수와 정수
    memo1 = list(map(int, input().split())) #수첩1
    memo1.sort()

    N2 = int(input()) #수첩 2에 적어 놓은 정수 개수와 정수
    memo2 = list(map(int, input().split())) #수첩2

    for num in memo2:
        if binary_search(memo1, num, N2):
            print(1)
        else:
            print(0)
            
    




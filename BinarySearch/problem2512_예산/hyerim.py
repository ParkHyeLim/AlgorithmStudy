#2512 예산(런타임 에러)

def binary_categories(arr, target, arr_len):
    result = 0
    start = min(arr)
    end = max(arr)

    while start <= end:
        total = 0 # 배정된 예산의 합
        mid = (start + end) // 2 # 중간점 찾기
        
        for i in range(arr_len):
            if arr[i] < mid:
                total += arr[i]
            else:
                total += mid
        
        if total <= target:
            result = mid # 예산 최댓값 갱신 
            start = mid + 1
        else:
            end = mid - 1

    return result

N = int(input()) #지방의 수
Budget = list(map(int, input().split())) #지방의 예산 요청
M = int(input()) #총 예산
Budget_limit = binary_categories(Budget, M, N)
print(Budget_limit)

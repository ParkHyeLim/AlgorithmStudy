#2805 나무 자르기(런타임 에러)
#min(H if (sum(arr-h) == M))

def binary_categories(arr, target, arr_len):
    result = 0
    start = min(arr)
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2 # 중간점 찾기

        total = 0 # 가져갈 나무 길이
        for i in range(arr_len):
            if arr[i] > mid:
                total += arr[i] - mid
        
        if total >= target:
            result = mid # 절단기 길이 최댓값 갱신 
            start = mid + 1
        else:
            end = mid - 1

    return result

N, M = map(int, input().split()) #나무 수, 필요한 나무 길이
tree_height = list(map(int, input().split()))
my_tree = binary_categories(tree_height, M, N)
print(my_tree)

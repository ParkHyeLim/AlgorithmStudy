# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# h = max(arr)
# result = M
# while h >= 0:
#     rs = 0
#     for i in range(N):
#         if arr[i]-h > 0:
#             rs += (arr[i] - h)

#     if rs >= M:
#         result = h
#         break
#     h -= 1

# print(result)

def bs(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        total = 0

        for x in arr:
            if x > mid:
                total += x - mid

        if total < m:
            end = mid-1
        else:
            res = mid
            start = mid + 1
    return res


n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = bs(arr, 0, max(arr))
print(result)

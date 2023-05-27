def bs(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        total = 0

        for x in arr:
            if x > mid:
                total += mid
            else:
                total += x

        if total <= M:
            start = mid + 1
        else:
            end = mid - 1
    return end


N = int(input())
arr = list(map(int, input().split()))
M = int(input())

result = bs(arr, 0, max(arr))
print(result)

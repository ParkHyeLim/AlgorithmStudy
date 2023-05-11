n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(k):
    max_idx = i
    for j in range(i, n):
        if arr[max_idx] < arr[j]:
            max_idx = j
    tmp = arr[i]
    arr[i] = arr[max_idx]
    arr[max_idx] = tmp

print(arr[k-1])
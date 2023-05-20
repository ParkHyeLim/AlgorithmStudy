N = int(input())
arr = list(map(int, input().split()))
M = int(input())
start = M // N
end = max(arr)
for i in range(start, end):
    rs = 0
    for i in range(len(arr)):
        rs += arr[i]

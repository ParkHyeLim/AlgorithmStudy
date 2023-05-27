T = int(input())

while T > 0:
    k = int(input())  # 층
    n = int(input())  # 호
    arr = [1 for i in range(n)]
    tmp = 0

    while k >= 0:
        for i in range(n-1):
            arr[i+1] = arr[i] + arr[i+1]
        k -= 1

    print(arr[n-1])
    T -= 1

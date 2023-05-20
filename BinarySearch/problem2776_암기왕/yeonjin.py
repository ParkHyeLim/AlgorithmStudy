T = int(input())
while T:
    N = int(input())
    arr1 = list(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    result = {}

    for i in arr2:
        result[i] = 0

    for i in arr1:
        if i in result:
            result[i] = 1

    for i in arr2:
        print(result[i])

    T -= 1

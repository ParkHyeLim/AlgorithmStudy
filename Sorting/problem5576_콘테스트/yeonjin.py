def getSum():
    arr = [0] * 10
    arr_sum = 0
    # 입력 받기
    for i in range(10):
        arr[i] = int(input())

    # 가장 큰 3개값 arr_sum에 더하기
    for i in range(3):
        max_idx = 0
        for j in range(10):
            if arr[max_idx] <= arr[j]:
                max_idx = j
        arr_sum += arr[max_idx]
        arr[max_idx] = 0
    return str(arr_sum)


print(getSum() + " " + getSum())

# 백설공주와 일곱난쟁이
arr = []
sum = 0
t1 = 0
t2 = 0

for i in range(9):
    n = int(input())
    arr.append(n)
    sum += n

found = False
for i in range(0, 8):
    for j in range(i, 9):
        if sum-arr[i]-arr[j] == 100 and i != j:
            t1 = i
            t2 = j
            break
    if found:
        break

for i in range(9):
    if i != t1 and i != t2:
        print(arr[i])

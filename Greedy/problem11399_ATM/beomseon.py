N = int(input())
arr =[]
arr = list(map(int, input().split()))
sum=0

arr.sort()
for i in range(1, N+1) :    
    for j in range(i) :     #각 사람이 돈을 인출하는데 필요한 시간
        sum += arr[j]
print(sum)
N, K = map(int, input().split())
arr =[]

for i in range(1, K+1) :
    arr.append(int(str(N*i)[: : -1]))

print(max(arr))
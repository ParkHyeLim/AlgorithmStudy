N, K = map(int, input().split())
arr=[]
for i in range (N) :
    arr.append(int(input()))

arr.reverse()

num=0
for i in arr:
    num += K//i
    K = K%i
print(num)
    

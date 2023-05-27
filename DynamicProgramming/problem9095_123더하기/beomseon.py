T = int(input())

num = [0]*11
num[1] = 1  # 1
num[2] = 2  # 1+1, 2
num[3] = 4  # 1+2,  1+1+1, 2+1,  3
for i in range(4, 11):
    num[i] = sum(num[i-3:i])  

for _ in range(T):
  n = int(input())
  print(num[n])
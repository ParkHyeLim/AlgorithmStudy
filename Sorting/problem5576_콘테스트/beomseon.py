W=[]
K=[]
W_sum=0
K_sum=0

for i in range(10):
  W.append(int(input()))
for i in range(10):
  K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

for i in range(3):
  W_sum += W[i]
  K_sum += K[i]

print(W_sum, K_sum)


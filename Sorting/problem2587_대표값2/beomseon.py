N=[]
for i in range(5):
   N.append(int(input()))

N.sort()

#평균
average = sum(N)//5

print(average)
print(N[2])

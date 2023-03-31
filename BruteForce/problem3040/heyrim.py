import random

list1 = []
listSum = []

for i in range(9):
    k = int(input())
    list1.append(k)

sum100 = 0

while((sum100 != 100)):
    listSum = random.sample(list1, k=7)
    sum100 = sum(listSum)


for i in listSum:
    print(i)
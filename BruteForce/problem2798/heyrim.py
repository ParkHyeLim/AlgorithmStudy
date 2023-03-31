import random

list1 = []
max_sum = 0

N, M = map(int, input().split(' '))
list2 = list(map(int, input().split(' ')))

for i in range(N*(N-1)*(N-2)):
    max_s = sum(random.sample(list2, k=3))
    if ((max_s > max_sum) & (max_s <= M)):
        max_sum = max_s

print(max_sum)
# 분해합
n = input()
length = len(n)
answer = 0

for i in range(1, int(n)):
    tmp = i
    sum = i
    for j in range(length):
        sum += (tmp % 10)
        tmp = int(tmp/10)
    if sum == int(n):
        answer = i
        break
print(answer)
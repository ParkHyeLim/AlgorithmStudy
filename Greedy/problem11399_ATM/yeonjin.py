n = int(input())
person = list(map(int, input().split()))
result = 0

for i in range(n):
    p = int(input())
    person.append(p)

person.sort()
for i in range(n):
    result += person[i]*(n-i)

print(result)

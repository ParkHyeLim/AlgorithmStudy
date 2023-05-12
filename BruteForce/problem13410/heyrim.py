# 1
N, K = map(int, input().split())

max_num = 0

for k in range(1, K+1):
    num = (N * k)
    ten = int(num/10)
    if (ten == 0):
        re_num = int(num % 10)
    else:
        re_num = int(str(int(num % 10)) + str(ten))

    if (re_num > max_num):
        max_num = re_num

print(max_num)

# 2
N, K = map(int, input().split())

max_num = 0

for k in range(1, K+1):
    num = (N * k)
    re_num = int(str(num)[::-1])
    if (re_num > max_num):
        max_num = re_num

print(max_num)

# 3
N, K = map(int, input().split())

max_num = 0

for k in range(1, K+1):
    num = (N * k)
    re_num = int(''.join(reversed(str(num))))
    if (re_num > max_num):
        max_num = re_num

print(max_num)

# 2, 3번 코드를 풀어쓴 풀이

N, K = map(int, input().split())
print(max([int(str(N * k)[::-1]) for k in range(1, K+1)]))

N, K = map(int, input().split())
print(max([int(''.join(reversed(str(N * k)))) for k in range(1, K+1)]))

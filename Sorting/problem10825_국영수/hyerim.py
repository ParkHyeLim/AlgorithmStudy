# 10825
# 국어, 영어, 수학
# 국어(내림차순), 영어(오름차순), 수학(내림차순)
# S를 최소로 하는 재배열 된 A

N = int(input())
Students_inf = []

for _ in range(N):
    name, Es, Ks, Ms = input().split()
    Students_inf.append([name, int(Es), int(Ks), int(Ms)])

Students_inf_sort = sorted(Students_inf, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(Students_inf_sort[i][0])

N = int(input())
lst = []
for i in range(N):
    name, kor, eng, math = input().split()
    lst.append([name, int(kor), int(eng), int(math)])

sorted_lst = sorted(lst, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(sorted_lst[i][0])
    

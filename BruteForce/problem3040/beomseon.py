# from itertools import combinations

# N_list = []
# for i in range (9) :
#     N_list.append(int(input()))

# for ans in combinations(N_list, 7) :
#     if sum(ans) == 100:
#         for i in ans:
#             print(i)
#         break

arr=[]
for i in range(9):
    arr.append(int(input()))

for i in range(9):
    for j in range(9):
        if sum(arr) - arr[i] - arr[j] == 100:
            x, y = i, j
            break
            
arr.remove(arr[x])
arr.remove(arr[y])
for i in arr:
    print(i)
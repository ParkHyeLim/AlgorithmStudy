n = int(input())
arr = [0]
max_score = 0

for i in range(n):
    a = int(input())
    arr.append(a)

stack = []
stack.append([0, 0, -1])  # index, score, jump(1칸 뛴 수)
while len(stack) != 0:
    idx, scr, jmp = stack[0]
    if jmp <= 0:     # 한 칸 점프
        if idx+1 == n:    # 마지막 칸 도착
            if max_score < scr + arr[idx+1]:
                max_score = scr + arr[idx+1]
        else:
            stack.append([idx+1, scr+arr[idx+1], jmp+1])

    if idx+2 == n and max_score < scr + arr[idx+2]:  # 두 칸 점프 & 마지막 칸 도착
        max_score = scr + arr[idx+2]
    elif idx+2 < n:   # 두 칸 점프
        stack.append([idx+2, scr+arr[idx+2], 0])
    stack.pop(0)

print(max_score)

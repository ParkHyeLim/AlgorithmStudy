# 5576
# W대학 / K대학
# 각 10명씩 참여
# 10명 중 가장 높은 3명의 점수 합

W_list = [int(input()) for _ in range(10)]
K_list = [int(input()) for _ in range(10)]

W_list.sort(reverse=True)
K_list.sort(reverse=True)

W_score = 0
K_score = 0

for i in range(3):
    W_score += W_list[i]
    K_score += K_list[i]

print("{} {}".format(W_score, K_score))
    



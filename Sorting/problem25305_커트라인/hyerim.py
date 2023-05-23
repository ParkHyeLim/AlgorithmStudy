# 25305
# N명의 학생
# 가장 높은 K명 상장 / 커트라인!

N, k = map(int, input().split())

score = [int(i) for i in input().split()]
score.sort(reverse=True)

cutLine = score[k-1]

print(cutLine)
    



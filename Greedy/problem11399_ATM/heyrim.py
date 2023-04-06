# N명의 사람
# 한명당 걸리는 시간 = P분
# 가장 빨리 끝나는 경우 = 오름차순으로 정렬했을 때

N = int(input())
n_mit = list(map(int, input().split()))
next_mit = 0
next_mit_list = []

n_mit.sort()

for i in range(len(n_mit)):
    next_mit += n_mit[i]
    next_mit_list.append(next_mit)


print(sum(next_mit_list))
    
    

#2775 부녀회장이 될거야

# a층 b호: a-1층(1~b호)의 합
def dynamic_calculation(floor, number):

    # 메모이제이션 테이블 초기화
    people = [[0]*(number+1) for _ in range(floor+1)]

    # 기저 조건 설정
    for i in range(1, number+1):
        people[0][i] = i

    # 하위 문제 해결
    for i in range(1, floor+1):
        underfloor = 0
        for j in range(1, number+1):
            underfloor += people[i-1][j]
            people[i][j] = underfloor
        
    return people[floor][number]

for _ in range(int(input())):
    k = int(input()) # k층
    n = int(input()) # n호
    print(dynamic_calculation(k, n))

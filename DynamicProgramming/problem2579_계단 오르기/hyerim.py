#2579 계단오르기
import random

# a층 b호: a-1층(1~b호)의 합
def dynamic_calculation(gameList, number):
    
    # 메모이제이션 테이블 초기화
    score = [0] * (number+1)
    
    # 기저 조건 설정
    score[1] = gameList[0]  
    score[2] = max(gameList[1], gameList[0]+gameList[1])
    # 이전 계단을 안 밟는 경우, 이전계단을 밟는 경우

    # 하위 문제 해결
    for i in range(3, number+1):
        score[i] = max(score[i-3]+gameList[i-2]+gameList[i-1], score[i-2]+gameList[i-1])
        # 이전계단을 밟는 경우(이이전 계단은 안 밟음), 이전 계단을 안 밟는 경우(이이전 계단은 밟음)

    return score[number]

number = int(input())
game = [int(input()) for _ in range(number)]
print(dynamic_calculation(game, number))

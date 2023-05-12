import sys

input = sys.stdin.readline  # 4652ms -> 500ms로 시간 개선됨

N = int(input())
data={}
for i in range(N):
    name, *score = input().split()  # unpacking 위해 *(askterlisk) 사용 -> input().split()의 결과 중 하나는 name으로 나머지는 score에 저장
    score = list(map(int, score))   # score리스트의 값들을 int형으로 변환하고 이 때 map객체로 반환되는 것을 list로 변경
    data[name] = score

sorted_data = sorted(data.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0])) 
for i in range(N):
    print(sorted_data[i][0])

# lambda함수(key) 이용하여 표현
# sorte에서 기준 값이 되는 x를 설정
# 국어점수 '감소' -> -x[1][0], 영어점수 '증가' -> x[1][1], 수학점수 '감소' -> -x[1][2], 이름 증가 -> x[0]  순서로
# data.items 형태 :dict_items([('Junkyu', [50, 60, 100]), ('Sangkeun', [80, 60, 50]) ...])


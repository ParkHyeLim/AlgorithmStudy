n = int(input())
#five_kg은 5키로봉지로 나눈 나머지
five_kg = n // 5

while five_kg >= 0:
    #reaminder : 남은 봉지수
    remainder = n - (5 * five_kg)
    if remainder % 3 == 0:
        print(five_kg + remainder // 3)
        break
    #나머지가 0이 아닐때 1을 빼주고 다시 시도
    five_kg -= 1
else:
    print(-1)

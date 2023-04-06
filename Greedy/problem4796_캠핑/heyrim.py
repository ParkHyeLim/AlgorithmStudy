# 연속하는 P일 = 20일
# L일 동안 사용 = 10일
# 이제 막 V일짜리 휴가 시작 = 28일

case_num = 1
while(True):
    # 입력
    L, P, V = map(int, input().split())
    # 0 3개를 입력 받으면 while문 탈출
    if (P == 0 & L == 0 & V == 0):
        break
    # camping이 가능한 일수 개산
    camping = (V // P)*L + min((V % P),L)
    # 출력(f-string)
    print(f"Case {case_num}: {camping}")
    # case +1
    case_num += 1

#9095 1, 2, 3 더하기

# n을 1, 2, 3의 합으로 나타내는 방법의 수
def dynamic_calculation(num):

    # 메모이제이션 테이블 초기화
    methods = [0] * 11

    # 기저 조건 설정
    methods[1] = 1 # 1을 만드는 경우의 수
    methods[2] = 2 # 2를 만드는 경우의 수
    methods[3] = 4 # 3을 만드는 경우의 수
    
    # 하위 문제 해결
    for i in range(4, num+1):
        methods[i] = methods[i - 1] + methods[i - 2] + methods[i - 3]
        # 각 숫자를 만들기 위해 이전 숫자에 대한 경우의 수를 모두 더해주는 것
        # 예) 6 = 5+1, 4+2, 3+3 / 7 = 6+1, 5+2, 4+3 
    
    return (methods[n])

for _ in range(int(input())):
    n = int(input()) # 구하고자 하는 수
    print(dynamic_calculation(n))

# 입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))
A.sort()			# binary search위해 정렬

for num in arrM:
    lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
    findNum = False		# 찾음 여부

    # binary serach
    while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2	
        if num == A[mid]:	# 찾으려고 하는 수가 mid와 같을 때
            findNum = True	
            print(1)		# 1 출력
            break		
        elif num > A[mid]:	# 찾으려고 하는 수가 mid보다 크다면
            lt = mid + 1	# lt를 mid보다 1크게해서 새로 설정된 lt와 rt사이에서 수 찾음
        else:			# 찾으려고 하는 수가 mid보다 작다면
            rt = mid - 1	# rt를 낮춤

    if not findNum:		# 찾지 못한 경우
        print(0)		# 0 출력
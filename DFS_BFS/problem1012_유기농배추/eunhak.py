T = int(input())

for i in range(T):
  
  M, N, K = map(int, input().split())
  
  # 배열 생성, 0으로 초기화
  arr=[[0 for j in range(N)] for i in range(M)]
  
  # 배추 심기
  for i in range(K):
    x, y = map(int,input().split())
    arr[x][y] = 1


  ### idea : (상,하,좌,우) 중 이미 탐색한 (상,좌)에 1이 있으면 세지 않는다
  count = 0 
  
  # out of index 에러 피하기 위해 예외처리
  # [0,0]
  if arr[0][0] == 1:   
    count += 1
  # 1열 : y=0
  for x in range(1,M):  
    if ( arr[x][0] == 1 ) & ( arr[x-1][0] != 1 ) :
      count += 1 
  # 1행 : x=0
  for y in range(1,N):  
    if ( arr[0][y] == 1 ) & ( arr[0][y-1] != 1 ) :
      count += 1

  # [1,1]부터 끝까지
  for x in range(1,M):
    for y in range(1,N):
      if  ( arr[x][y] == 1 ) & ( arr[x-1][y]!= 1 ) & ( arr[x][y-1]!=1 ) :
        count += 1

  print(count)
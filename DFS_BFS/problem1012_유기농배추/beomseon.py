# dfs 풀이
import sys
sys.setrecursionlimit(10000)  #런타임 에러 방지 위해 재귀 limit 설정

# dfs 정의
def dfs(y, x):
    # 상하좌우 확인을 위해 dx, dy 생성
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):  # nx:ny -> M:N 범위
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1  # 방문 체크
                dfs(ny, nx)         # 재귀함수 통해 상하좌우 방향으로 붙어있는 배추를 모두 방문가능
               
T = int(input())  #테스트 케이스 개수
for i in range(T):
    M, N, K = map(int, input().split())  # M:가로길이: x(열), N:세로길이: y(행), K:개수
    graph = [[0]*M for i in range(N)] # 3x5 
    cnt = 0

    for j in range(K):
        X, Y = map(int, input().split())    # 배추의 위치
        graph[Y][X] = 1                     # x축: 열, y축: 행
   
    # dfs 활용해서 배추 그룹 수 세기
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                graph[y][x] == -1 # 방문 체크
                dfs(y, x)
                cnt += 1

    print(cnt)
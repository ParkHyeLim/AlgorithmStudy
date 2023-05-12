global mp, visit, dx, dy
MAX = 51
mp = [[0]*MAX]*MAX
visit = [[False]*MAX]*MAX
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
global M, N, K, column, row, cnt

# 세로, 가로


def dfs(x, y):
    # 시작지점을 방문했다고 체크
    visit[x][y] = True
    for k in range(4):
        # 다음 좌표값을 정해주고
        nx = x + dx[k]
        ny = y + dy[k]
        # 다음 방향이 범위 내에 있다면
        if 0 <= nx and nx < N and 0 <= ny and ny < M:

            # 그 방향이 배추가 있고, 방문하지 않았다면
            if mp[nx][ny] and visit[nx][ny] == False:
                visit[nx][ny] = True
                # 탐색
                dfs(nx, ny)


def init():
    for i in range(N):
        for j in range(M):
            mp[i][j] = 0
            visit[i][j] = False


# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 대로 입력을 받음
while T > 0:
    cnt = 0
    init()
    M, N, K = map(int, input().split())
    # 배추가 있는 좌표 입력
    for i in range(K):
        # 가로, 세로 입력순
        column, row = map(int, input().split())
        if 0 <= column and column < M and 0 <= row and row < N:
            mp[row][column] = 1
    for i in range(N):
        for j in range(M):
            # 배추가 심어져 있는 곳부터 dfs탐색시작
            if mp[i][j] and visit[i][j] == False:
                dfs(i, j)
                # 지렁이 추가
                cnt += 1
    # 지렁이 출력
    print(cnt)
    T -= 1
